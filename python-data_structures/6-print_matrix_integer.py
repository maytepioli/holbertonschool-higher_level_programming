#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for line in matrix:
        for element  in line:
            print("{:d}".format(element), end=" ")
        print()