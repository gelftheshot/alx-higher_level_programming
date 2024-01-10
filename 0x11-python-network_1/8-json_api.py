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
    try:
        jfile = r.json()
        if jfile != {}:
            print("[{}] {}".format(jfile['id'], jfile['name']))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
