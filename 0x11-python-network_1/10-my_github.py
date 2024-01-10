#!/usr/bin/python3
"""Write a Python script that takes your GitHub credentials
(username and password)"""
import sys
import requests

if __name__ == "__main__":
    r = requests.get("https://api.github.com/user", auth=(sys.argv[1], sys.argv[2]))
    rjson = r.json()
    print(rjson.get('id'))
