import requests
from bs4 import BeautifulSoup

def fetch_scholar(username: str):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"
        }

        # Step 1: Search for the author
        query = username.replace(" ", "+")
        search_url = f"https://scholar.google.com/citations?view_op=search_authors&mauthors={query}"
        response = requests.get(search_url, headers=headers)
        if response.status_code != 200:
            return {"error": f"Scholar search failed: status {response.status_code}"}

        soup = BeautifulSoup(response.text, "html.parser")
        profile_tag = soup.select_one("div.gs_ai_t a")

        if not profile_tag or not profile_tag.get("href"):
            return {"error": "No author profile found"}

        profile_url = f"https://scholar.google.com{profile_tag['href']}"

        # Step 2: Scrape publications from the profile
        profile_response = requests.get(profile_url, headers=headers)
        if profile_response.status_code != 200:
            return {"error": f"Profile page fetch failed: status {profile_response.status_code}"}

        profile_soup = BeautifulSoup(profile_response.text, "html.parser")
        rows = profile_soup.select("tr.gsc_a_tr")

        publications = []
        for row in rows[:10]:  # Top 10 publications
            title_tag = row.select_one(".gsc_a_at")
            year_tag = row.select_one(".gsc_a_y span")

            publications.append({
                "title": title_tag.text if title_tag else "No title",
                "year": year_tag.text if year_tag else "N/A"
            })

        return {
            "query": username,
            "profile_url": profile_url,
            "publication_count": len(publications),
            "publications": publications
        }

    except Exception as e:
        return {"error": f"Scholar scraping failed: {str(e)}"}
