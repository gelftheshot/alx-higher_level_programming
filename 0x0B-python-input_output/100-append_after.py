#!/usr/bin/python3

""" a function that that apped after a certain line """


def append_after(filename="", search_string="", new_string=""):
    """ the function starts here to serach and replace
    Args:
        filename (str) - is the file name
        search_string (str) - the serhcering string
        new_string  (str) - the string to be written
    """
    with open(filename, "r", encoding="utf-8") as file:
        data = file.read()

    with open(filename, "a+", encoding="utf-8") as f:
        for line in data:
            f.write(line)
            f.write("\n")
            if line == search_string:
                f.write(new_string)
                f.write("\n")
