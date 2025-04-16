from app.fetchers.github import fetch_github
from app.fetchers.linkedin import fetch_linkedin
from app.fetchers.scholar import fetch_scholar
from app.models import ResumeFetchRequest

def aggregate_resume_data(request: ResumeFetchRequest):
    data = {}

    if request.github:
        data["github"] = fetch_github(request.github)

    if request.linkedin:
        data["linkedin"] = fetch_linkedin(request.linkedin)

    if request.linkedin:
        data["scholar"] = fetch_scholar(request.scholar)

    return data

