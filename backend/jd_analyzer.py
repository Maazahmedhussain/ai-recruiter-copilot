import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def analyze_jd(jd_text):

    prompt = f"""
Extract the following from the job description:

1. Skills
2. Tools
3. Experience
4. Responsibilities

Return JSON format.

Job Description:
{jd_text}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content