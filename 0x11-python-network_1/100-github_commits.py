#!/usr/bin/python3
"""A Python script that returns some API about commit history."""
import requests
import sys

if __name__ == "__main__":
    repo_url = sys.argv[2]
    repo_name = sys.argv[1]
    url = f"https://api.github.com/repos/{repo_url}/{repo_name}/commits"

    r = requests.get(url)
    rjson = r.json()

    for i, item in enumerate(rjson):
        if i < 10:
            print(f"{item['sha']}: {item['commit']['author']['name']}")
        else:
            break
