#!/usr/bin/python3
"""a Python script that takes in a URL and an email
sends a POST request to the passed URL"""
import sys
import urllib.request
import urllib.parse
if __name__ == "__main__":
    data = {"email" : sys.argv[2]}
    data = urllib.parse.urlencode(data)
    data = data.encode('ascii')
    req = urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlopen(req) as file:
        print(file.read().decode("utf-8"))
