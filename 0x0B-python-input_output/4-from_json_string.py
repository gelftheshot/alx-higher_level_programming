#!/usr/bin/python3

""" json working module """
import json


def from_json_string(my_str):
    """ convert json form to python object form """
    return json.loads(my_str)
