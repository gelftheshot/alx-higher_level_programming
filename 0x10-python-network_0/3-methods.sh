#!/bin/bash
#Writing a Bash script that takes in a URL and displays all HTTP methods the server will accept.
curl -sI "$1" | grep -Fi "allow" | cut -d" " -f2-
