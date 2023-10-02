#!/usr/bin/python3

""" representing a class Rectangle """


class Rectangle():
    """Rectangle class that defines """

    def __init__(self, width=0, height=0):
        """ initilizing the class rectangle

        Args:
            height (int) - is height of the rectangel
            width (int) - is the width of the rectangel
        """

        self.height = height
        self.width = width

    @property
    def width(self):
        """ Get the width of the rectangle """
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        "Get the height of the rectangle"
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
