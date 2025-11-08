import json
import re

# Function to get JSON from CV text
def extract_cv_json(cv_text, client):
    prompt = f"""
    You are an AI assistant that extracts structured information from resumes/CVs.
    Your task is to read the CV text below and output **valid JSON only** with the keys: 
    - name
    - skills
    - experience
    - education

    Requirements:
    1. **Skills** must be a list of unique items (no duplicates). Include technical skills, tools, programming languages, frameworks, or domain knowledge inferred from the text.
    2. **Experience** should summarize relevant work experience, including years and roles if mentioned. Infer the relevance if not explicit.
    3. **Education** should capture formal degrees, certifications, or equivalent relevant training. If the CV does not explicitly mention a degree but shows relevant expertise (e.g., AI, Machine Learning, Deep Learning), describe it in a concise way.
    4. If a field is not explicitly stated, infer it from context in a reasonable way. Do not invent unrelated information.
    5. Do not include extra text or commentary — output **JSON only**.

    Example output format:
    {{
      "name": "Alice Smith",
      "skills": ["Python", "SQL", "Tableau", "Machine Learning"],
      "experience": "3 years as Data Analyst focusing on predictive modeling",
      "education": "BSc Computer Science or equivalent AI-related expertise"
    }}

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
