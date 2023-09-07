#!/usr/bin/python3

if __name__ == "__main__":

    import sys

    x = len(sys.argv)
    sum = 0

    if x > 1:
        for i in range(1, x):
            sum = sum + int(sys.argv[i])

    print(sum)
