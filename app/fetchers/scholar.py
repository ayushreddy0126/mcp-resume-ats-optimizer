def fetch_scholar(username: str):
    #Siumulated Google scholar data
    return {
        "citations" : 128,
        "h_index": 6,
        "i10_index": 3,
        "publications": [
            {"title": "Optimizing Resume Parsing with LLMs", "year": 2024},
            {"title": "MCP Architectures in Modern Applications", "year": 2025}
        ]
    }