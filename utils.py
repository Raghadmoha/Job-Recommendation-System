import PyPDF2 # a library to turn text inside pdf files into a Python string
import os
from dotenv import load_dotenv

#Load API key
def load_api_key():
    load_dotenv()
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    if not GEMINI_API_KEY:
        raise ValueError("API key not found! Check your .env file.")
    return GEMINI_API_KEY

# Extract text from PDF
def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, "rb") if isinstance(pdf_path, str) else pdf_path as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text
    return text