#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for line in matrix:
        for element in line:
            if element == line[-1]:
                print("{:d}".format(element), end="")
            else:
                print("{:d}".format(element), end=" ")
        print()
