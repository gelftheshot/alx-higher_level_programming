#!/usr/bin/python3

""" the functon that returns the divided martix """

def matrix_divided(matrix, div):
    """the function returns the new matrix which the argumet
        matrix divided by argumet div
        Args:
            matrix (list of list) - is the orginal matrix
            div (int or float) - the number that divides the mat
    """
    if (not isinstance(matrix , list) ) or (not all(isinstance(i, list) for i in matrix)) or (not all(isinstance(k ,int) for ele in matrix for i in ele)):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    a = len(matrix[0])
    if not all(a == len(row) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not (isinstance(div , int) or isinstance(div float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")


