#!/usr/bin/bash
# Write a Bash script that takes in a URL, sends a request to that URL

curl -Is "$1" | grep -Fi "Content-Length" | cut -d' ' -f2
