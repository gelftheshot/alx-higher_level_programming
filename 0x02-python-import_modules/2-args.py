#!/usr/bin/python3

if __name__ == "__main__":

    from sys import argv
    x = len(argv)
    if x == 1:
        print("0 arguments.")
    else:
        print("{} argument:".format(x - 1))
        for i in range(x-1):
            print("{}: {}".format(i+1, argv[i + 1]))
