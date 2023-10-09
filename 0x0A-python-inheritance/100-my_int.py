#!/usr/bin/python3

""" a class MyInt """


class MyInt(int):
    """ a class that inherit from int but reverse == and != """

    def __eq__(self, __value: object):
        return super().__ne__(__value)

    def __ne__(self, __value: object):
        return super().__eq__(__value)
