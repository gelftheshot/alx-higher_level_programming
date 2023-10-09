#!/usr/bin/python3

"""a Rectangle class that inherts for mbase_geometry class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """initign a rectangle class that inherts from baseGeometyr calss"""

    def __init__(self, width, height):
        """ ininting a rectangel attributes with and hight
            Args:
                width(int) - the width of the rectangle
                height(int) - is the hight of the recatangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """ returns the are of the ractangle"""
        return (self.__width * self.__height)

    def __str__(self):
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
