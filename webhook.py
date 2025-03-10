import requests
import datetime

WEBHOOK_URL = "https://rnd-assignment.automations-3d6.workers.dev/"

def send_webhook(name, email, cv_data, cv_url):
    payload = {
        "cv_data": {
            "personal_info": {"name": name, "email": email},
            "education": cv_data["education"],
            "qualifications": cv_data["qualifications"],
            "projects": cv_data["projects"],
            "cv_public_link": cv_url
        },
        "metadata": {
            "applicant_name": name,
            "email": email,
            "status": "prod",
            "cv_processed": True,
            "processed_timestamp": datetime.datetime.utcnow().isoformat()
        }
    }
    headers = {"X-Candidate-Email": email}
    requests.post(WEBHOOK_URL, json=payload, headers=headers)
