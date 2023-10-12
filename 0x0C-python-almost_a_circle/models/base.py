#!/usr/bin/python3

""" init the base class base of all other class """


class Base:
    """ the base created here """
    __nb_objects = 0

    def __init__(self, id=None):
        """ initing a calss base object
        Args:
            id(int) - the unique number to the object
        """

        if (id is not None):
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
