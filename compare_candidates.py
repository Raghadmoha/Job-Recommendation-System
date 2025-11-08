import json
from utils import extract_text_from_pdf
# Function to parse required skills, experience, education from job description text
def parse_job_description(job_text):
    lines = job_text.splitlines()
    skills, experience, education = [], None, None
    for line in lines:
        line = line.strip()
        if line.startswith("-"):
            if "years" in line.lower():
                experience = line
            elif "bsc" in line.lower() or "msc" in line.lower():
                education = line
            else:
                # assume skill
                skills.append(line.replace("-", "").strip())
    return {
        "skills": skills,
        "experience": experience,
        "education": education
    }

# Function to score a candidate
def score_candidate(cv_json, job_req):
    score = 0
    # Skills match
    cv_skills = [s.lower() for s in cv_json["skills"]]
    job_skills = [s.lower() for s in job_req["skills"]]
    for skill in job_skills:
        if skill in cv_skills:
            score += 1

    # Experience match (simple check: years in text)
    if job_req["experience"]:
        job_years = int(''.join(filter(str.isdigit, job_req["experience"])))
        cv_years_list = [int(s) for s in cv_json["experience"].split() if s.isdigit()]
        if cv_years_list and cv_years_list[0] >= job_years:
            score += 1

    # Education match
    if job_req["education"]:
        if job_req["education"].lower() in cv_json["education"].lower():
            score += 1

    return score

# Function to rank all candidates
def rank_candidates(cv_json_list, job_text):
    job_req = parse_job_description(job_text)
    scores = []
    for cv in cv_json_list:
        s = score_candidate(cv, job_req)
        scores.append({"name": cv["name"], "score": s})
    # Sort descending by score
    ranked = sorted(scores, key=lambda x: x["score"], reverse=True)
    return ranked

#Example (as file path)
if __name__ == "__main__": 
    # Load job description
     job_text = extract_text_from_pdf("jobdescription.pdf") 
     # Load CV JSONs (from extract_info.py output) \
     with open("cv1.json", "r") as f:
         cv1_json = json.load(f)
     with open("cv2.json", "r") as f: 
         cv2_json = json.load(f)
         
         ranked = rank_candidates([cv1_json, cv2_json], job_text)
         print("Candidate Ranking:") 
         for r in ranked:
             print(f"{r['name']}: {r['score']} points")
