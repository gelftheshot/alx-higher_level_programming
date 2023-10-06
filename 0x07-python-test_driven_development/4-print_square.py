#!/usr/bin/python3

""" this is a function that prints # square of size size """


def print_square(size):
    """ the function stats herer

        Args:
            size (int) : the size(length and width )
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0 and isinstance(size, float):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print("")
