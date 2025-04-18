import gspread
from google.oauth2.service_account import Credentials

SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
SPREADSHEET_ID = "1TwjErpxpMgEfw7jk6fEZxBd3rLzDNknf3Bw90ChA0Vc"

creds = Credentials.from_service_account_file("credentials.json", scopes=SCOPES)
client = gspread.authorize(creds)

def upload_to_google_sheets(name, email, phone, cv_data, cv_url):
    sheet = client.open_by_key(SPREADSHEET_ID).sheet1
    sheet.append_row([name, email, phone, str(cv_data["education"]), str(cv_data["qualifications"]), str(cv_data["projects"]), cv_url])
