## Job Application Form

### 🎯 Project Description
The **Job Application Processing App** is a web-based system that automates job application handling. It allows applicants to submit their details and upload CVs, which are then stored in **AWS S3**. The app extracts key information (education, qualifications, projects) from the CV and saves it to **Google Sheets**. A **webhook notification** sends the processed data to an external API, and a **follow-up email** is sent to applicants the next day. This solution streamlines recruitment by reducing manual effort and ensuring efficient applicant tracking. 

### 🚀 How to Run this App

#### 1. Install the Python (If not installed)
Check your python version:
-python --version

#### 2. Clone the Github Repository

#### 3. Create Virtual Environment
python -m venv venv
---
-source venv/bin/activate  # For macOS/Linux
---
-venv\Scripts\activate     # For Windows


#### 4. Install Dependencies
pip install -r requirements.txt


#### 5. Run the Application 
python app.py
