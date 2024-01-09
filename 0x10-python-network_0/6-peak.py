#!/usr/bin/python3

""" a code that find the max of an arry in the fastest way """
def find_peak(list_of_integers):
    """ finding the max of the array """
    new_list = sorted(list_of_integers)
    if len(new_list) > 1:
        return new_list[-1]
