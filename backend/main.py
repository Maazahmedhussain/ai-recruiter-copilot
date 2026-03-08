from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import shutil
from jd_analyzer import analyze_jd

from resume_parser import extract_resume_text

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

@app.post("/upload-resume")
async def upload_resume(file: UploadFile = File(...)):

    file_location = f"temp_{file.filename}"

    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    resume_text = extract_resume_text(file_location)
    @app.post("/analyze-jd")
async def analyze_job_description(jd: str):

    result = analyze_jd(jd)

    return {
        "analysis": result
    }

    return {
        "filename": file.filename,
        "resume_preview": resume_text[:500]
    }