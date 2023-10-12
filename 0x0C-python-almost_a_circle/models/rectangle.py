#!/usr/bin/python3

""" this is the rectangle class that inherts from the base calss """
from models.base import Base


class Rectangle(Base):
    """ the rectangle class started here """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ this function init the attributes of the objects
        Args:
            width (int) - is the width of the rectangle
            height (int) - is the height of the rectangle
            x (int) - is the x conrdinate of the rectangle
            y (int) - the y cordinate of where the rectangle startt
            id (int) - is the unique number of the class
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ get or set the width """
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ set or get the height """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ getting or setting the x cord """
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        """ getting or setting the y cord """
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ is the are of the rectangle """
        return self.__width * self.__height

    def display(self):
        """ this is the display function that display #"""
        for i in range(self.__y - 1):
            print("")

        for i in range(self.__height):
            print(" " * self.__x, end="")
            for j in range(self.__width):
                print("#", end="")
            print("")

    def __str__(self):
        """ return the printable format for the function"""
        s = "[Rectangle] (" + str(self.id) + ") "
        s += str(self.__x) + "/" + str(self.__y)
        s += " - " + str(self.__width) + "/" + str(self.__height)
        return (s)
