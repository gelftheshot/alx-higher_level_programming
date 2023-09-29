#!/usr/bin/python3

"""  a function that prints a text with 2 new lines after each of these characters: ., ? and : """

def text_indentation(text):
    """ a function starts here
        Args:
            text (str) is a string of text
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    delma = ".?:"
    t = 1
    for char in text:
        if (not char in delma) and t:
            print(char, end="")
            t = 1
        elif char in delma:
            print(char)
            print("")
            t = 0
        else:
            if char != " ":
                print(char)
            t = 1
