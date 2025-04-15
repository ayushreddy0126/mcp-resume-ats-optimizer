def fetch_github(username : str):
    # Simulated Github data

    return {
        "username" : username,
        "projects" : [
            {"name" : "resume-optimizer", "stars" : 150, "language": "Python"},
            {"name" : "llm-orchestrator", "stars": 87,"language":"TypeScript"}
        ],
        "contributions" : 324,
        "followers" : 45
    }