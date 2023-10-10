#!/usr/bin/python3


def write_file(filename="", text=""):
    """ write to file truncating the existing thing """
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
