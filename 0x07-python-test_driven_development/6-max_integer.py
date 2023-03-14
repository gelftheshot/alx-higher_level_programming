#!/usr/bin/python3

"a function that finds the maximum value of the list"


def max_integer(list=[]):
    """ defing a function.
    Args:
        list - the the list
    """

    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1
    return result
