#!/usr/bin/python3


def append_write(filename="", text=""):
    """ append text at the end of the file """
    with open(filename, "a"):
        return (filename.append(text))
