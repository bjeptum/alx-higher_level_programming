#!/usr/bin/python3
"""
Computes the square value of integers
of a matrix
"""


def square_matrix_simple(matrix=[]):
    result = [[i ** 2 for i in row] for row in matrix]
    return result
