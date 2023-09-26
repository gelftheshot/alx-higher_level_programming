#!/usr/bin/python3

"""a python class that defins a square"""


class Square:
    """a calss that represents a Square"""

    def __init__(self, size=0):
        """ the function intent to inin some parameters
        of the instance attributes
        Args:
            size (int): is th size of the Square
        """
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not (isinstance(value, int)):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """a funtion that returns the area of Square
        Args: None
        """
        return (self.__size * self.__size)

    def my_print(self):
        """ a function that prints # of the square """
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print("")
        if self.__size == 0:
            print("")
