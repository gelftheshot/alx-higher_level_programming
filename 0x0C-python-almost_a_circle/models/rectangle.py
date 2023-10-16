#!/usr/bin/python3

""" this is the rectangle class that inherts from the base calss """
from models.base import Base

""" the rectangle calss is starting here """


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
        if type(value) is not int:
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
        if type(value) is not int:
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
        if type(value) is not int:
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
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ is the are of the rectangle """
        return self.width * self.height

    def display(self):
        """ this is the display function that display #"""
        for i in range(self.y):
            print("\n", end="")

        for i in range(self.height):
            print(" " * self.x, end="")
            for j in range(self.width):
                print("#", end="")
            print("")

    def __str__(self):
        """ return the printable format for the function"""
        s = "[Rectangle] (" + str(self.id) + ") "
        s += str(self.x) + "/" + str(self.y)
        s += " - " + str(self.width) + "/" + str(self.height)
        return (s)

    def update(self, *args, **kwargs):
        """ updeate the attribues based on args
        Args:
            *args - are the list of value of attributes
            **kwargs is the key value pair
        if *args exit and not empty, kwargs should be skipped
        """
        if ((args is not None) and (len(args) != 0)):
            for i in range(len(args)):
                if i == 0:
                    if args[i] is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = args[i]
                if i == 1:
                    self.width = args[i]
                if i == 2:
                    self.height = args[i]
                if i == 3:
                    self.x = args[i]
                if i == 4:
                    self.y = args[i]
        else:
            if (type(kwargs) is dict):
                for key, value in kwargs.items():
                    if (key == "id"):
                        if value is None:
                            w = self.width
                            h = self.height
                            self.__init__(w, h, self.x, self.y)
                        else:
                            self.id = value
                    if (key == "width"):
                        self.width = value
                    if (key == "height"):
                        self.height = value
                    if (key == "x"):
                        self.x = value
                    if (key == "y"):
                        self.y = value

    def to_dictionary(self):
        """Return the dictionary representation of a Rectangle."""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
