# LLM-Powered Job Recommendation System 💼🤖

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

1. Create a `.env` file in the project root and add your Gemini API key:

GEMINI_API_KEY=your_api_key_here


2. Install the required Python packages using:

```bash
py -m pip install -r requirements.txt
```
Required packages:

PyPDF2 → Read text from PDFs (CVs and job descriptions)

python-dotenv → Load Gemini API key securely from .env

google-genai → Official Gemini SDK to interact with the Gemini API

streamlit → Web interface for uploading files and displaying results

⚙️ How It Works
1. Extract CV Information

extract_info.py reads CV text and sends it to the Gemini API, which outputs structured JSON containing:

name

skills (list of unique skills, tools, programming languages, etc.)

experience (years and roles)

education (degrees or relevant expertise, inferred if necessary)

2. Compare Candidates

compare_candidates.py reads the job description and extracts required skills, experience, and education.

Each candidate is scored:

Skills match → +1 per matching skill

Experience match → +1 if candidate experience meets or exceeds requirement

Education match → +1 if degree matches

Candidates are ranked in descending order of total score.

3. Streamlit Web App

Upload job description PDF and multiple CV PDFs.

Extract JSON for each CV.

Rank candidates and display results interactively.

📥 Running the Project

Command-line Execution:

py extract_info.py
py compare_candidates.py
streamlit run app.py

📝 Notes

The Gemini API is required to convert unstructured CV text into structured JSON that the model can understand.

Install Gemini SDK if not already installed:

py -m pip install google-genai

Ensure your .env file contains:

GEMINI_API_KEY=your_api_key_here

The system is fully modular, so you can easily add new scoring rules, handle more file formats, or integrate with other models.

Enjoy exploring this AI-powered Job Recommendation System, test it with different CVs and job descriptions, and see how AI can help streamline candidate selection! 🌟


