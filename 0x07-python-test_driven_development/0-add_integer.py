#!/usr/bin/python3
# 0-add_integer.py

def add_integer(a, b=98):
    """take two numbers and return their sum

        Args:
            a (int) - is the first number
            b(int) - is the second number with option 98
    """

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
