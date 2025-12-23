import json
import re

# Function to get JSON from CV text
def extract_cv_json(cv_text, client):
    prompt = f"""
You are an AI assistant specialized in extracting structured information from resumes/CVs. 
Your goal is to read the CV text below and return **only valid JSON** with the following keys:

- "name": Full name of the candidate.
- "skills": List of unique skills, tools, programming languages, frameworks, or domain expertise inferred from the CV.
- "experience": A concise summary of relevant work experience, including years and roles if mentioned.
- "education": Formal degrees, certifications, or equivalent relevant training. If a degree is not explicitly mentioned, summarize relevant expertise.

Important instructions:

1. Output **JSON only** — no extra text or commentary.
2. Deduplicate skills; include all relevant technical or domain knowledge.
3. For experience, extract the number of years if mentioned and highlight relevant roles.
4. For education, capture degrees, certifications, or summarize relevant expertise if a degree is missing.
5. **Infer relevant expertise**: 
   - If the CV contains skills or projects related to a field (e.g., NLP, Machine Learning, PyTorch) but does not explicitly state a job title (e.g., "AI Engineer"), infer the candidate’s relevant expertise and include it in experience/education if appropriate.
   - Avoid inventing unrelated information; only infer expertise from the CV content.
6. Be precise, concise, and factual.

CV Text:
{cv_text}
"""


    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    # Extract JSON from response
    match = re.search(r"\{.*\}", response.text, re.DOTALL)
    if match:
        return json.loads(match.group(0))
    else:
        raise ValueError("Could not extract JSON from Gemini response")
