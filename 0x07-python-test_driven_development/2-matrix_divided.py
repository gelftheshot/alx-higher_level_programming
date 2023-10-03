#!/usr/bin/python3

""" the functon that returns the divided martix """


def matrix_divided(matrix, div):
    """the function returns the new matrix which the argumet
        matrix divided by argumet div
        Args:
            matrix (list of list) - is the orginal matrix
            div (int or float) - the number that divides the mat
    """

    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(element, int) or isinstance(element, float))
                    for element in [k for row in matrix for k in row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(i/div, 2) for i in row] for row in matrix]
