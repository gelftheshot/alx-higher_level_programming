#!/usr/bin/pyhton3

"""a python class that defins a square"""


class Square:
    """a calss that represents a Square"""

    def __init__(self, size):
        """ the function intent to inin some parameters of
        the instance attributes
        Args:
            size (int): is th size of the Square
        """
        self.__size = size
