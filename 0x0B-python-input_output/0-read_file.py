#!/usr/bin/python3


def read_file(filename=""):
    """ read from file and return the file contant
        Args:
            filename (str) - is the name of the file
    """
    with open(filename, "r", encoding="utf-8") as file:
        tom = file.read()
        print(tom)
