#!/usr/bin/python3

"""reprsenting my list  class"""


class MyList(list):
    "reprseting a class that inhertes a list class"

    def print_sorted(self):
        """ a function that areturn the sorted list"""
        print(sorted(self))