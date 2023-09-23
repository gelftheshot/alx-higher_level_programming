#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_mat = [x**2 for ele in matrix for x in ele]
    return new_mat
