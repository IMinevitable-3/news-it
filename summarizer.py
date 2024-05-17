import requests

body = """
"""
resp = requests.post(
    "https://api.smrzr.io/v1/summarize?num_sentences=10&algorithm=kmeans&min_length=20&max_length=200",
    data=body,
)
summary = resp.json()
print(summary)
