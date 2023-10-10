#!/usr/bin/python3

""" defing a fucntion that represting a list pascal"""


def pascal_triangle(n):
    """ the function starts here
    Args:
        n(int) - the pascals triangle
    """

    prev = [1, 1]
    new = []
    answer = []
    if (n <= 0):
        return ([])
    if n == 1:
        return ([[1]])
    answer.append([1])
    answer.append(prev)

    for i in range(2, n):
        for j in range(i+1):
            if (j == 0 or j == i):
                new.append(1)
            else:
                new.append(prev[j] + prev[j-1])
        answer.append(new)
        prev = new
        new = []
    return (answer)
