#!/usr/bin/python3

""" a code that find the max of an arry in the fastest way """
def find_peak(list_of_integers):
    """ finding the max of the array """
    x = len(list_of_integers)
    if (x == 0):
        return None
    if (x == 1):
        return list_of_integers[0]
    if (x == 2):
        return max(list_of_integers)
    middle = x//2
    if (list_of_integers[middle] > list_of_integers[middle+1] and list_of_integers[middle - 1]):
        return list_of_integers[middle]
    if list_of_integers[middle+1] > list_of_integers[middle]:
        return find_peak(list_of_integers[middle:])
    return find_peak(list_of_integers[:middle])
