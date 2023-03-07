#!/usr/bin/python3
# 2-uniq_add.py

def uniq_add(my_list=[]):
    sum = 0
    for i in set(my_list):
        sum = sum + i
    return (sum)
