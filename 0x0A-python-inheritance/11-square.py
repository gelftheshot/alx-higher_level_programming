#!/usr/bin/python3

""" a calss rectangle that inherts a square class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ reprsenting a rectangle class """

    def __init__(self, size):
        """ ininting a square attributes
        Args:
            size(int) - is the size of the square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        return "[Square] " + str(self.__width) + "/" + str(self.__height)
