#!/usr/bin/pyhton3

"""a python class that defins a square"""


class Square:
    """a calss that represents a Square"""

    def __init__(self, size=0):
        """ the function intent to inin some parameters
        of the instance attributes
        Args:
            size (int): is th size of the Square
        """
        if not (isinstance(size, int)):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
