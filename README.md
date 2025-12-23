# LLM-Powered Job Recommendation System 💼

This project is a **job recommendation system** that automatically extracts information from CVs and ranks candidates based on a job description using the **Gemini AI API**. It provides a fully automated pipeline: **PDF → JSON → Scoring → Ranking**, and is easy to extend for multiple CVs or different job descriptions.

---

## 🚀 Key Features

- **Automated Pipeline**: Convert CVs and job descriptions from PDF to structured JSON, score candidates, and generate a ranking.  
- **Accurate Extraction**: Uses **Gemini API** to extract structured information (skills, experience, education) from unstructured CV text.  
- **Flexible & Scalable**: Supports multiple CVs and various job descriptions.  
- **Secure API Handling**: Gemini API key is loaded securely from `.env`.  

---

## 📂 Project Structure

- `extract_info.py` → Extracts structured data from CVs using Gemini API.  
- `compare_candidates.py` → Compares candidates against a job description and ranks them based on scoring.  
- `utils.py` → Helper functions for loading API keys and extracting text from PDFs.  
- `app.py` → Streamlit web app for uploading job descriptions and CVs and viewing candidate rankings.  
- `.env` → Stores your **Gemini API key** (do not share this file).  
- Sample PDFs → `jobdescription.pdf`, `cv1.pdf`, `cv2.pdf`.  
- Generated JSON → `cv1.json`, `cv2.json` (created automatically from `extract_info.py`).  

---

## 🔧 Setup & Environment
Ensure you provide your api key:
GEMINI_API_KEY=
and
Install the required Python packages using:

```bash
py -m pip install -r requirements.txt
