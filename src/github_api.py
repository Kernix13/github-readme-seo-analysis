# These are part of Python
import os
import base64

from dotenv import load_dotenv
import requests
import pandas as pd

# Do I need this:
# os.makedirs("data", exist_ok=True)

load_dotenv()
TOKEN = os.getenv("GITHUB_TOKEN")

# Basic API Setup
HEADERS = {"Authorization": f"token {TOKEN}", "Accept": "application/vnd.github+json"}


# Fetch Repo Data
def get_repo_data(repo_full_name):
    url = f"https://api.github.com/repos/{repo_full_name}"
    response = requests.get(url, headers=HEADERS)

    if response.status_code != 200:
        return None

    return response.json()


# Fetch README + Word Count
def get_readme_word_count(repo_full_name):
    url = f"https://api.github.com/repos/{repo_full_name}/readme"
    response = requests.get(url, headers=HEADERS)

    if response.status_code != 200:
        return 0

    content = response.json().get("content", "")
    decoded = base64.b64decode(content).decode("utf-8", errors="ignore")

    return len(decoded.split())


# Combine Everything
def analyze_repo(repo):
    repo_data = get_repo_data(repo)
    if not repo_data:
        return None

    return {
        "repo": repo,
        "word_count": get_readme_word_count(repo),
        "forks": repo_data.get("forks_count", 0),
        "stars": repo_data.get("stargazers_count", 0),
        "topics": len(repo_data.get("topics", [])),
        "about_text": repo_data.get("description", ""),
    }


# Run on your repo list
repos = [
    "vizzuhq/ipyvizzu-story",
    "vonj/snippets.org",
    "vs4vijay/typescript-express-template",
    "w3cj/express-api-starter-ts",
    "w3tecch/express-graphql-typescript-boilerplate",
    "wms2537/nodejs-jwt-auth",
    "worldbank/template",
    "xtreamsrl/jupytemplate",
    "yeasin2002/react-ts-starter",
    "YounesseElkars/Express-Prisma-TypeScript",
    "youssefbennour/AspNetCore.Starter",
    "zestgeek/Auth-using-Vuejs-express-jwt-nodejs",
    "zmts/supra-api-nodejs",
]

results = []

for repo in repos:
    data = analyze_repo(repo)
    if data:
        results.append(data)

# Convert to DataFrame
df = pd.DataFrame(results)
df.to_csv("data/github_repo_metadata.csv", index=False)

# I need additional fields returned in analyze_repo(repo)
