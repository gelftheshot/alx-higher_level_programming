#!/usr/bin/python3

"""a function that returns the list of available
    attributes and methods of an object """


def lookup(obj):
    """ function return list of available methos
    Args:
        obj - is the object variable
    """
    return dir(obj)
