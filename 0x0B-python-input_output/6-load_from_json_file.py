#!/usr/bin/python3

"""this is the json library """
import json

""" defining a functiont that just load from a json file"""


def load_from_json_file(filename):
    """ defing a function that does load from filename
    Args:
        filename - the name of the file
    """
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
