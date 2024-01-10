#!/usr/bin/python3
"""a Python script that fetches url status using request"""
import requests
if __name__ == "__main__":
    r = requests.get("https://alx-intranet.hbtn.io/status")
    val = r.text
    print("Body response:")
    print("\t- type: {}".format(type(val)))
    print("\t- content: {}".format(val))
