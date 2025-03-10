import pdfplumber
from docx import Document

def extract_cv_data(file_path):
    data = {"education": [], "qualifications": [], "projects": []}

    if file_path.endswith(".pdf"):
        with pdfplumber.open(file_path) as pdf:
            text = " ".join([page.extract_text() for page in pdf.pages if page.extract_text()])
    elif file_path.endswith(".docx"):
        doc = Document(file_path)
        text = " ".join([p.text for p in doc.paragraphs])

    # Simple keyword-based extraction (can be improved using NLP)
    if "Education" in text:
        data["education"].append(text.split("Education")[1].split("\n")[0])
    if "Projects" in text:
        data["projects"].append(text.split("Projects")[1].split("\n")[0])

    return data
