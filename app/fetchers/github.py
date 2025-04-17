import requests
import os

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

def fetch_github(username : str):

    headers = {
        "Accept" : "application/vnd.github+json"
    }

    if GITHUB_TOKEN:
        headers["Authorization"] = f"Bearer {GITHUB_TOKEN}"
    

    user_url = f"https://api.github.com/users/{username}"
    repos_url = f"https://api.github.com/users/{username}/repos"

    user_resp = requests.get(user_url, headers=headers)
    repos_resp = requests.get(repos_url, headers=headers)


    if user_resp.status_code != 200 or repos_resp.status_code != 200:
        return {"error":"GitHub API request failed",
                "user_status": user_resp.status_code,
            "repos_status": repos_resp.status_code}
    
    user_data = user_resp.json()
    repos_data = repos_resp.json()

    return {
        "username": user_data.get("login"),
        "followers": user_data.get("followers"),
        "public_repos": user_data.get("public_repos"),
        "projects":[
            {
            "name": repo["name"],
            "description": repo.get("description"),
            "stars": repo.get("stargazers_count",0),
            "language": repo.get("language")
            }
            for repo in repos_data
        ]

    }

    
    
    

    