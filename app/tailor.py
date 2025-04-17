# app/tailor.py
from fastapi import APIRouter, UploadFile, Form
from fastapi.responses import JSONResponse
from llm.tailor_llm import tailor_resume_with_llm
import pdfplumber
import io

router = APIRouter()

@router.post("/resume/tailor")
async def tailor_resume(resume_file: UploadFile, job_description: str = Form(...)):
    try:
        contents = await resume_file.read()
        with pdfplumber.open(io.BytesIO(contents)) as pdf:
            resume_text = "\n".join(page.extract_text() or "" for page in pdf.pages)

        tailored_resume = tailor_resume_with_llm(resume_text, job_description)
        return {"tailored_resume": tailored_resume}

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
