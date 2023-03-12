#!/usr/bin/python3
# 2-rectangel.py

"""defing the class rectangele"""


class Rectangle:
    """repersents a rectangle..."""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ initilizing the class rectangle

        Args:
            height (int) - is height of the rectangel
            width (int) - is the width of the rectangel
        """

        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """ Get/set the width of the rectangle """
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
        "Get/set the height of the rectangle"
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """return the are of the rectangel"""
        return (self.__width * self.__height)

    def perimeter(self):
        """returns the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """prints the # reperesentation of the recatangel"""
        if self.__height == 0 or self.width == 0:
            return ""
        arr = []
        for i in range(self.__height):
            for j in range(self.__width):
                arr.append(str(self.print_symbol))
            if (i != self.height-1):
                arr.append("\n")
        return ("".join(arr))

    def __repr__(self):
        "return a string used as a call for the second time"
        arr = "Rectangle(" + str(self.__width)
        arr += "," + str(self.__height) + ")"
        return (arr)

    def __del__(self):
        """Print a message for every deletion of a Rectangle."""
        print("Bye rectangle...")
        type(self).number_of_instances -= 1
