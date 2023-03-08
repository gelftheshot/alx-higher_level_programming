#!/usr/bin/python3
# 0-safe_print_list.py

def safe_print_list(my_list=[], x=0):

    tot = 0
    for i in range(len(my_list)):
        try:
            print("{}".formate(my_list[i]), end = "")
            tot = tot + 1
        except IndexError:
            break
    print("")
    return (tot)
