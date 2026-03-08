def calculate_match(jd_skills, resume_text):

    resume_text_lower = resume_text.lower()

    matched = []
    missing = []

    for skill in jd_skills:
        if skill in resume_text_lower:
            matched.append(skill)
        else:
            missing.append(skill)

    if len(jd_skills) == 0:
        score = 0
    else:
        score = int((len(matched) / len(jd_skills)) * 100)

    return {
        "match_score": score,
        "matched_skills": matched,
        "missing_skills": missing
    }