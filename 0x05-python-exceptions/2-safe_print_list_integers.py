#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    num = 0
    loop = 0
    while (loop < x):
        try:
            print("{:d}".format(my_list[loop]), end="")
            num += 1
            loop += 1
        except (TypeError, ValueError):
            loop += 1
            continue
    print("")
    return (num)
