#!/usr/bin/python3
def print_last_digit(number):
    if number >= 0:
        print(f"{number % 10}", end="")
        return number % 10
    if number < 0:
        print(f"{number * -1}", end="")
        return (-1 * number) % 10
