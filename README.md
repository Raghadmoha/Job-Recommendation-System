- Setup and Environment(We installed necessary Python packages):
⋆ PyPDF2 → to read text from PDF files (CVs and job description)
⋆ python-dotenv → to securely load the Gemini API key from .env
⋆ google-genai → official Gemini SDK to interact with the Gemini API

- Created the following project files:
⋆ extract_info.py → extracts structured data
⋆ compare_candidates.py → compares CVs against job description and ranks candidates
⋆ .env → stores the Gemini API key securely (not to be shared)
⋆ Sample PDFs: jobdescription.pdf, cv1.pdf, cv2.pdf.
⋆ JSON files (generated automatically): cv1.json, cv2.json

- Comparing candidates:
⋆ Read job description text and extracted required skills, experience, and education 
⋆ Scored each candidate based on:
 Skills match → +1 per matching skill
 Experience match → +1 if candidate experience meets or exceeds requirement
 Education match → +1 if degree matches
⋆ Ranked candidates in descending order of total score

- To Summarize; the project's key features:
⋆ Fully automated pipeline: PDF → JSON → scoring → ranking.

⋆ Easy to extend for multiple CVs and different job descriptions.

⋆ Gemini API ensures accurate extraction of structured information from CVs.

⋆ Secure handling of API key using .env.

Notes:
- In the extract_info.py file:
we need an official Gemini SDK(Software Development Kit) (google-genai) so we install running this in the terminal: py -m pip install google-genai
The reason we need it is to use it to extract structured JSON 
and the reason we need to turn unstructured text into structered JSON so that a model(like Gemini) can understand
so in order to do this we use Gemini API key and send a prompt asking to extract

- You can install packages using:
py -m pip install -r requirements.txt

- To run:
py extract_info.py
py compare_candidates.py
streamlit run app.py


cd "C:\Users\ECC\OneDrive\Documents\AI Bootcamp IEEE\Project 3\Job-Recommendation-System"
