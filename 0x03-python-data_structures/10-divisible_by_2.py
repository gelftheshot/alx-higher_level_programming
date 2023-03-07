#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    a_list = []
    for mem in my_list:
        if mem % 2 == 0:
            a_list.append(True)
        else:
            a_list.append(False)
    return (a_list)
