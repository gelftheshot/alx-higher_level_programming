#!/usr/bin/python3

""" reprsnting a a function that add attribute if possble"""


def add_attribute(a_class, attr, value):
    """ adding a attribut if possible"""
    if hasattr(a_class, "__dict__"):
        setattr(a_class, attr, value)
    else:
        raise TypeError("can't add new attribute")
