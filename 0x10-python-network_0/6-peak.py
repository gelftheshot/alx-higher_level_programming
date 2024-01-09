#!/usr/bin/python3

""" a code that find the max of an arry in the fastest way """
def find_peak(list_of_integers):
    """ finding the max of the array """
    if (len(list_of_integers) == 0):
        return None
    if (len(list_of_integers) == 1):
        return list_of_integers[0]
    a = find_peak(list_of_integers[:len(list_of_integers)//2])
    b = find_peak(list_of_integers[len(list_of_integers)//2:])
    if a > b:
        return a
    return b
