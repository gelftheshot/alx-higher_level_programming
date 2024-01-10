#!/usr/bin/python3
"""Write a Python script that takes your GitHub credentials
(username and password)"""
import sys
import requests

if __name__ == "__main__":
    url = "https://api.github.com/user"
    auth = (sys.argv[1], sys.argv[2])
    r = requests.get(url, auth=auth)
    rjson = r.json()
    print(rjson.get('id'))
