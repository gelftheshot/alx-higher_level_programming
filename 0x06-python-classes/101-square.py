#!/usr/bin/python3

"""a python class that defins a square"""


class Square:
    """a calss that represents a Square"""

    def __init__(self, size=0, position=(0, 0)):
        """ the function intent to inin some parameters
        of the instance attributes
        Args:
            size (int): is th size of the Square
            position (int, int) the potion of top of squre
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """get or set the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        if not (isinstance(value, int)):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """get or set the postion of the square"""
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """a funtion that returns the area of Square
        Args: None
        """
        return (self.__size * self.__size)

    def my_print(self):
        """ a function that prints # of the square """
        if self.__size == 0:
            print("")
            return

        for g in range(self.__position[1]):
            print("")
        for i in range(self.__size):
            for k in range(self.__position[0]):
                print(" ", end="")
            for j in range(self.__size):
                print("#", end="")
            print("")

    def __str__(self):
        """Define the print() representation of a Square."""
        if self.__size != 0:
            [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            if i != self.__size - 1:
                print("")
        return ("")
