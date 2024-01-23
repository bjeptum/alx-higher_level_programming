#!/usr/bin/python3
"""
Prints a matrix of integers
"""


def print_matrix_integer(matrix=[[]]):
    length = len(matrix)
    for i in range(length):
        for j in range(len(matrix[i])):
            print("{:d}".format(matrix[i][j]), end="")
            if j != len(matrix[i]) - 1:
                print(" ", end="")
        print()
