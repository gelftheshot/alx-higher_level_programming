#!/usr/bin/python3
matrix_mul = __import__('100-matrix_mul').matrix_mul
a = [[1, 2, 3],
     [4, 5, 6]]
b = [[9, 8],
     [7, 6],
     [5, 4]]
c = [[0, 0],
     [0, 0]]
d = [[0, 0, 0],
     [0, 0, 0]]
e =  [[1, 0, 0, 0],
     [0, 1, 0, 0],
     [0, 0, 1, 0],
     [0, 0, 0, 1]]
f = [[1, 0, 0, 0],
     [0, 1, 0, 0],
     [0, 0, 1, 0],
     [0, 0, 0, 1]]
g = [[5, 2, 8],
     [1, 7, 3]]
h = [[9, 4],
     [6, 2],
     [0, 3]]
print(matrix_mul(a,b))
print(matrix_mul(c,d))
print(matrix_mul(e,f))
print(matrix_mul(g,h))

