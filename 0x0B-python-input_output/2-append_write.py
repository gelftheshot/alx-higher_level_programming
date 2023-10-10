#!/usr/bin/python3


def append_write(filename="", text=""):
    """ append text at the end of the file
        Args:
            filename(str) - the name of the file
            text(str) - the text to be appened
    """
    with open(filename, "a", encoding="utf-8"):
        return (filename.append(text))
