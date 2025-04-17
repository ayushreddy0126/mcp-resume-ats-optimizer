import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def tailor_resume_with_llm(original_resume, job_description):
    prompt = f"""
    You are an expert resume writer. Given this resume and job description, rewrite the resume so that it highlights relevant skills, experience, and keywords to improve ATS match.

    Resume:
    {original_resume}

    Job Description:
    {job_description}

    Rewrite the resume below:
    """

    response = client.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages = [{"role":"user", "content": prompt}]
    )

    return response.choices[0].message.content


