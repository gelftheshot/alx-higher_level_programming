#!/usr/bin/python3
def uppercase(str):
    for let in str:
        if ord(let) >= 97 and ord(let) <= 122:
            print(chr(ord(let) - 32),end="")
        else:
            print(let,end="")
    print()
uppercase("gelf is good 88 AbcdD")
