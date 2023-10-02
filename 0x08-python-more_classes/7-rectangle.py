#!/usr/bin/python3

""" representing a class Rectangle """


class Rectangle():
    """Rectangle class that defines a rectangle """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ initilizing the class rectangle

        Args:
            height (int) - is height of the rectangel
            width (int) - is the width of the rectangel
        """

        self.height = height
        self.width = width
        type(self).number_of_instances += 1

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
        li = []
        for i in range(self.__height):
            for j in range(self.__width):
                li.append(str(self.print_symbol))
            if (i != self.height-1):
                li.append("\n")
        return ("".join(li))

    def __repr__(self):
        """ eturn a string representation of the rectangle to be able
          to recreate a new instance by using eval()"""
        tom = str(self.__class__.__name__) + "(" + str(self.width)
        tom += "," + str(self.height) + ")"
        return (tom)

    def __del__(self):
        """delet rectangle and print message"""
        print("Bye rectangle...")
        type(self).number_of_instances -= 1
