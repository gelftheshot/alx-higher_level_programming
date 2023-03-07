#!/usr/bin/python3
# 9-multiply_by_2.py

def multiply_by_2(a_dictionary):
    new_dick = {}

    new_dick = [x: a_dictionary[x]*2 for x in a_dictionary]
    return new_dick
