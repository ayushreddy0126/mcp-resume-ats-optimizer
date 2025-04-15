from app.fetchers.github import fetch_github
from app.fetchers.linkedin import fetch_linkedin
from app.fetchers.scholar import fetch_scholar

def aggregate_resume_data(platforms: list, username: str):
    data = {}

    if "github" in platforms:
        data["github"] = fetch_github(username)

    if "linkedin" in platforms:
        data["linkedin"] = fetch_linkedin(username)

    if "scholar" in platforms:
        data["scholar"] = fetch_scholar(username)

    return data

