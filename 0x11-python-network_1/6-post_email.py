#!/usr/bin/python3
"""a Python script that takes in a URL and an email address
sends a POST request to the passed URL"""
import sys
import requests
if __name__ == "__main__":
    val = {"email": sys.argv[2]}
    r = requests.post(sys.argv[1], data=val)
    print(r.text)
