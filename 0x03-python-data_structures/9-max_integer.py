#!/usr/bin/python3
# 9-max_integer.py

def max_integer(my_list=[]):

    if len(my_list) == 0:
        return None
    a = my_list[0]

    for i in range(1, len(my_list)):
        if my_list[i] > a:
            a = my_list[i]
    return (a)
