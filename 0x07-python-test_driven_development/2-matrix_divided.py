#!/usr/bin/python3
""" Divides elements of a matrix """


def matrix_divided(matrix, div):
    """ Function that divides all the elements of a matrix
    Return: A new matrix"""

    # Check if matrix is a list of lists
    if not isinstance(matrix, list) or not all(
            isinstance(row, list) for row in matrix):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )

    # Check if each row of the matrix is of the same size
    if len(matrix) > 0:
        row_length = len(matrix[0])
        if not all(len(row) == row_length for row in matrix):
            raise TypeError(
                "Each row of the matrix must have the same size"
            )

    # Check if matrix elements are integers or floats
    if not all(
        isinstance(cell, (int, float)) for row in matrix for cell in row
    ):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )

    # Check if div is a number
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check if div is not zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Perform division and rounding
    return [
        [round(cell / div, 2) for cell in row] for row in matrix
    ]
