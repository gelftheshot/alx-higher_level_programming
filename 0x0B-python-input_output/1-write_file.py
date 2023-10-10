#!/usr/bin/python3


def write_file(filename="", text=""):
    """ write to file truncating the existing thing
        Args:
            filename (str) - is the name of the file
            text (str) - the text to be wrtten
    """
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
