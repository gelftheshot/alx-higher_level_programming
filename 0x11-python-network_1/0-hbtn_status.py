#!/usr/bin/python3

""""defing a code that fentch a website"""
import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as file:
        file = file.read()
        print("Body response:")
        print("\t- type: {}".format(type(file)))
        print("\t- content: {}".format(file))
        print("\t- utf8 content: {}".format(file.decode('utf-8')))
