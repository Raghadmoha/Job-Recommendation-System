import json
import re

#Function to get JSON from CV text
def extract_cv_json(cv_text, client):
    prompt = f"""
    Extract the candidate information from the text below.
    Output **valid JSON only**, with keys: name, skills, experience, education.
    - Skills must be a list of unique items (no repeats)
    - Do not add extra text
    - Example output format:
      {{
        "name": "Alice Smith",
        "skills": ["Python", "SQL", "Tableau"],
        "experience": "3 years as Data Analyst",
        "education": "BSc Computer Science"
      }}

    Text:
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