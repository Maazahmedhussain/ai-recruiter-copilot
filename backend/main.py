from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import shutil

from resume_parser import extract_resume_text
from jd_analyzer import analyze_jd
from match_engine import calculate_match
from resume_optimizer import generate_resume_suggestions


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {"message": "AI Recruiter Copilot API running"}


# Upload Resume Endpoint
@app.post("/upload-resume")
async def upload_resume(file: UploadFile = File(...)):

    file_location = f"temp_{file.filename}"

    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    resume_text = extract_resume_text(file_location)

    return {
        "filename": file.filename,
        "resume_preview": resume_text[:500]
    }


# JD Analysis Endpoint
@app.post("/analyze-jd")
async def analyze_job_description(jd: str):

    jd_data = analyze_jd(jd)

    return {
        "jd_skills": jd_data["skills"]
    }


# Resume Match Endpoint
@app.post("/match")
async def match_resume(jd: str, file: UploadFile = File(...)):

    file_location = f"temp_{file.filename}"

    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Extract resume text
    resume_text = extract_resume_text(file_location)

    # Analyze JD
    jd_data = analyze_jd(jd)

    # Calculate match
    match_result = calculate_match(jd_data["skills"], resume_text)

    # Generate resume improvement suggestions
    suggestions = generate_resume_suggestions(
        match_result["missing_skills"]
    )

    return {
        "jd_skills": jd_data["skills"],
        "match_result": match_result,
        "resume_suggestions": suggestions
    }