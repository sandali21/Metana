from flask import Flask, render_template, request, redirect, url_for, session
import os
import json
import googleapiclient.discovery
import google.auth.transport.requests
from google.oauth2.service_account import Credentials
from google_sheets import upload_to_google_sheets
from webhook import send_webhook
from send_email import send_followup_email
from extract_cv import extract_cv_data

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Secure key for session management
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

GOOGLE_CREDENTIALS_FILE = "credentials.json"
SCOPES = ["https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/spreadsheets"]
creds = Credentials.from_service_account_file(GOOGLE_CREDENTIALS_FILE, scopes=SCOPES)
drive_service = googleapiclient.discovery.build("drive", "v3", credentials=creds)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        file = request.files["cv"]

        if file:
            file_path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
            file.save(file_path)

            # Upload CV to Google Drive
            file_metadata = {"name": file.filename}
            media = googleapiclient.http.MediaFileUpload(file_path, mimetype="application/pdf")
            uploaded_file = drive_service.files().create(body=file_metadata, media_body=media).execute()

            cv_url = f"https://drive.google.com/file/d/{uploaded_file['id']}/view"

            # Extract CV Data
            cv_data = extract_cv_data(file_path)

            # Store data in Google Sheets (replace with your function)
            upload_to_google_sheets(name, email, phone, cv_data, cv_url)

            # Send Webhook
            send_webhook(name, email, cv_data, cv_url)

            # Schedule Email
            send_followup_email(email, name)


            return render_template('index.html', success=True)

    return render_template("index.html", success=False)


if __name__ == "__main__":
    app.run(debug=True)
