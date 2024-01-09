#!/usr/bin/env bash
# Write a Bash script that takes in a URL, sends a request to that URL
# and display the size of the body in byte

curl -is "$1" | grep -Fi "Content-Length"
