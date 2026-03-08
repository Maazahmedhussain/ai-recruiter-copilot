import re

def analyze_jd(jd_text):

    # simple keyword list
    skills_list = [
        "python",
        "sql",
        "aws",
        "azure",
        "terraform",
        "kubernetes",
        "docker",
        "informatica",
        "spark",
        "hadoop",
        "java",
        "snowflake"
    ]

    jd_text_lower = jd_text.lower()

    found_skills = []

    for skill in skills_list:
        if skill in jd_text_lower:
            found_skills.append(skill)

    return {
        "skills": found_skills
    }