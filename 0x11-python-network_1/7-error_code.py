#!/usr/bin/python3
"""a Python script that fetches url status using request"""
import requests
import sys
if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    if r.status_code < 400:
        print(r.text)
    else:
        print("Error code: {}".format(r.status_code))
