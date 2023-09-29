#!/usr/bin/python3
""" this is the functin that return the full name from the first and lat name """

def say_my_name(first_name, last_name=""):
    """this function prints full name by taking first and last name as
        an arguement
        Args:
        first_name(str) - is the first name
        last_name(str) - is the last name
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
