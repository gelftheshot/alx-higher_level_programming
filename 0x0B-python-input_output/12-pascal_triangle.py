#!/usr/bin/python3


def pascal_triangle(n):
    prev = [1, 1]
    new = []
    answer = []
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
