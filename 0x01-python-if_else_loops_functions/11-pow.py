#!/usr/bin/python3
def pow(a, b):
    pro = 1
    if b >= 0:
        for i in range(b):
            pro = pro * a
        return pro
    else:
        for i in range(-1 * b):
            pro = pro * a
        return 1 / pro
