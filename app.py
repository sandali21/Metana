from flask import Flask, render_template, request, redirect, url_for
import os
import boto3
from extract_cv import extract_cv_data
from google_sheets import upload_to_google_sheets
from webhook import send_webhook
from send_email import send_followup_email

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Configure AWS S3
S3_BUCKET = "your-s3-bucket-name"
s3 = boto3.client("s3", aws_access_key_id="YOUR_ACCESS_KEY", aws_secret_access_key="YOUR_SECRET_KEY")

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

            # Upload CV to S3
            s3.upload_file(file_path, S3_BUCKET, file.filename)
            cv_url = f"https://{S3_BUCKET}.s3.amazonaws.com/{file.filename}"

            # Extract CV Data
            cv_data = extract_cv_data(file_path)

            # Store in Google Sheets
            upload_to_google_sheets(name, email, phone, cv_data, cv_url)

            # Send Webhook
            send_webhook(name, email, cv_data, cv_url)

            # Schedule Email
            send_followup_email(email, name)

            return redirect(url_for("index"))
    
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
