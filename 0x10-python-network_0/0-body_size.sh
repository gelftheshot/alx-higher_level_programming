#!/usr/bin/bash
# Write a Bash script that takes in a URL, sends a request to that URL

curl -is "$1" | grep -Fi "Content-Length"
