import streamlit as st
from utils import extract_text_from_pdf, load_api_key
from extract_info import extract_cv_json
from compare_candidates import rank_candidates
from google import genai

# Load API key
GEMINI_API_KEY = load_api_key()
client = genai.Client(api_key=GEMINI_API_KEY)


st.title("LLM-Powered Job Recommendation System")

# Upload job description
job_file = st.file_uploader("Upload Job Description PDF", type="pdf")

# Upload one or more CVs
cv_files = st.file_uploader("Upload CV(s) PDF", type="pdf", accept_multiple_files=True)

if job_file and cv_files:
    job_text = extract_text_from_pdf(job_file)
    
    cv_json_list = []
    for cv_file in cv_files:
        cv_text = extract_text_from_pdf(cv_file)
        cv_json = extract_cv_json(cv_text, client)
        cv_json_list.append(cv_json)
        st.write(f"Extracted JSON for {cv_file.name}:")
        st.json(cv_json)

    # Rank candidates
    ranked = rank_candidates(cv_json_list, job_text)
    st.subheader("Candidate Ranking:")
    for r in ranked:
        st.write(f"{r['name']}: {r['score']} points")
