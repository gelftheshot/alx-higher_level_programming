#!/usr/bin/python3
# 9-multiply_by_2.py

def multiply_by_2(a_dictionary):
    new_dick = {}

    new_dick = list(map(lambda x : a_dictionary[x]*2, a_dictionary])
    return new_dick
