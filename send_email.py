import smtplib
from email.mime.text import MIMEText

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_SENDER = "sandalimahi43@gmail.com"
EMAIL_PASSWORD = "Sandali2000"

def send_followup_email(email, name):
    subject = "Your CV is Under Review"
    body = f"Hello {name},\n\nThank you for submitting your application. Your CV is under review, and we will get back to you soon."

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = EMAIL_SENDER
    msg["To"] = email

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(EMAIL_SENDER, EMAIL_PASSWORD)
        server.sendmail(EMAIL_SENDER, email, msg.as_string())
