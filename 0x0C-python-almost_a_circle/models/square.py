#!/usr/bin/python3

from models import rectangle
Rectangle = rectangle.Rectangle


class Square(Rectangle):
    """ this is the place of documentation"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get/set the size of the Square."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """ this is the comment section belive it or not"""
        s = "[Square] (" + str(self.id) + ") "
        s += str(self.x) + "/" + str(self.y)
        s += " - " + str(self.size)
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
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = args[i]
                if i == 1:
                    self.size = args[i]
                if i == 2:
                    self.x = args[i]
                if i == 3:
                    self.y = args[i]
        else:
            if (type(kwargs) is dict) and (len(kwargs) != 0) and \
                    (kwargs is not None):
                for key, value in kwargs.items():
                    if (key == "id"):
                        if value is None:
                            w = self.width
                            h = self.height
                            self.__init__(w, h, self.x, self.y)
                        else:
                            self.id = value
                    if (key == "size"):
                        self.size = value
                    if (key == "x"):
                        self.x = value
                    if (key == "y"):
                        self.y = value

    def to_dictionary(self):
        """Return the dictionary representation of the Square."""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }
