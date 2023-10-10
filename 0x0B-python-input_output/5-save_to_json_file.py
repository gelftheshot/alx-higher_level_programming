#!/usr/bin/python3

""" this is a json library """
import json

"""defing a function that save python obj as a json file """


def save_to_json_file(my_obj, filename):
    """ save an object as a json gile """

    with open(filename, "w", encoding="utf-8") as file:
        json.dump(my_obj, file)
