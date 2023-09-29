#!/usr/bin/python3

""" a function that adds two integers """


def add_integer(a, b=98):
    """ return the sum intiger of two numbers
        Args:
            a (int or float) - the first number
            b (int or float) - the second number
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
