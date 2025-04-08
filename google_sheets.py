import gspread
from google.oauth2.service_account import Credentials

SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
SPREADSHEET_ID = "1044381972066-9hg5fqrkid60vefnnt85mm104ggpuo6b.apps.googleusercontent.com"

creds = Credentials.from_service_account_file("credentials.json", scopes=SCOPES)
client = gspread.authorize(creds)

def upload_to_google_sheets(name, email, phone, cv_data, cv_url):
    sheet = client.open_by_key(SPREADSHEET_ID).sheet1
    sheet.append_row([name, email, phone, str(cv_data["education"]), str(cv_data["qualifications"]), str(cv_data["projects"]), cv_url])
