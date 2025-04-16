import requests

def fetch_linkedin(username: str):
    api_key = "cjQYXwBIl5-mSQrZjyZ8sg"
    profile_url = f"https://www.linkedin.com/in/{username}/" if "http" not in username else username

    response = requests.get(
        "https://nubela.co/proxycurl/api/v2/linkedin",
        headers={"Authorization": f"Bearer {api_key}"},
        params={"url": profile_url}
    )

    if response.status_code != 200:
        return {"error": f"Proxycurl failed with status {response.status_code}"}

    data = response.json()
    return {
        "profile_url": profile_url,
        "name": data.get("full_name"),
        "headline": data.get("occupation"),
        "experiences": [job.get("title") for job in data.get("experiences", []) if job.get("title")]
    }
