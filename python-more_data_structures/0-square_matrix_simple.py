#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix2 = []
    for line in matrix:
        matrix_new = []
        for element in line:
            matrix_new.append(element**2)
        matrix2.append(matrix_new)
    return matrix2
