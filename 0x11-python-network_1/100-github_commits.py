#!/usr/bin/python3
""" a python script that returns some api about commit history """
import requests
import sys

if __name__ == "__main__":
    url = "https://api.github.com/repos/" + sys.argv[2] + "/" + sys.argv[1] + "/commits"
    r = requests.get(url)
    rjson = r.json()

    j = 0
    for i in rjson:
        if (j < 10):
            print("{}: {}".format(i['sha'], i['commit']['author']['name']))
            j += 1
        else:
            break

