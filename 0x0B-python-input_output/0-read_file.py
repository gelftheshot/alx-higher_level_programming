#!/usr/bin/python3


def read_file(filename=""):
    """ read from file and return the file contant """
    with open(filename, "r") as file:
        tom = file.read()
        print(tom, end="")
