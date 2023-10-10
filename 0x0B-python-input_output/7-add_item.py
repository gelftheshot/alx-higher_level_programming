#!/usr/bin/python3

import json
import sys
import os
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


if not (os.path.exists("add_item.json")):
    ma_list = []
else:
    with open("add_item.json", "r", encoding="utf-8") as file:
        ma_list = load_from_json_file("add_item.json")

for i in range(len(sys.argv)):
    ma_list.append(sys.argv[i])

with open("add_item.json", "w", encoding="utf-8") as file:
    save_to_json_file(ma_list, file)

