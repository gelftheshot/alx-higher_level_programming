#!/usr/bin/python3
"""a Python script that takes in a URL and an email address
sends a POST request to the passed URL"""
import sys
import requests
if __name__ == "__main__":
    if len(sys.argv) < 2:
        val = {"q": ""}
    else:
        val = {"q": sys.argv[1]}
    r = requests.post("http://0.0.0.0:5000/search_user", data=val)
    jfile = r.json()
    if isinstance(jfile, dict) and jfile != {}:
        print("[{}] {}".format(jfile['id'], jfile['name']))
    elif jfile == {}:
        print("No result")
    else:
        print("Not a valid JSON")
