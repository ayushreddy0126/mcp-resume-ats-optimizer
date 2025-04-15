from fastapi import FastAPI
from app.models import ResumeFetchRequest, ResumeData
from app.aggregator import aggregate_resume_data

app = FastAPI()

@app.get("/")
def root():
    return {"message": "MCP Resume Aggregator is running 🚀"}

@app.post("/resume/fetch", response_model=ResumeData)
def fetch_resume_data(request: ResumeFetchRequest):
    result = aggregate_resume_data(request.platforms, request.username)
    return result
