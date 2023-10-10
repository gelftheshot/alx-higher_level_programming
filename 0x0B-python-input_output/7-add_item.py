#!/usr/bin/python3

"""this is just a sys module """
import sys

if __name__ == '__main__':
    save_to_json = __import__('5-save_to_json_file').save_to_json_file
    load_from_json = __import__('6-load_from_json_file').load_from_json_file

try:
    ma_list = load_from_json("add_item.json")
except FileNotFoundError:
    ma_list = []

for i in range(1, len(sys.argv)):
    ma_list.append(sys.argv[i])

save_to_json(ma_list, "add_item.json")
