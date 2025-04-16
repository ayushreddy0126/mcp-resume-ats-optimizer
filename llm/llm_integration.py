from openai import OpenAI
from dotenv import load_dotenv
import requests
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_AI_KEY"))



def call_mcp_api(github=None, linkedin=None, scholar=None):
    url = "http://127.0.0.1:8001/resume/fetch"
    payload = {
        "github": github,
        "linkedin": linkedin,
        "scholar": scholar
    }
    response = requests.post(url, json=payload)
    return response.json()

#Asking openAI to generate a resume summary for MCP response
def generate_resume_text(resume_data):
    prompt = f"""
    You are a resume writing assistant. Bsed on the following data aggregated from Github, LinkedIn, and Google Scholar,
    write a professional resume summary for the person. Focus on skills, experience, and achievements.

    Resume Data:
    {resume_data}
    """

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content

# Test the end-to-end pipeline
if __name__ == "__main__":
    resume_data = call_mcp_api(
        github = "ayushreddy0126",
        linkedin = "https://www.linkedin.com/in/ayushreddy0126/",
        scholar = "Ayush Reddy"
    )

    summary_text = generate_resume_text(resume_data)

    print("\n Resume Summary: \n")
    print(summary_text)

