#!/usr/bin/python3
"""
Module that multiplies 2matrices
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using NumPy.

    Args:
        m_a: The first matrix.
        m_b: The second matrix.

    Returns:
    The result of the matrix multiplication.
    """
    # Validate input types
    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise TypeError("Both arguments must be lists of lists")
    
    try:
        # Convert lists of lists to NumPy arrays
        arr_a = np.array(m_a)
        arr_b = np.array(m_b)
    except Exception as e:
        raise TypeError("Invalid input matrices") from e
    
    try:
        # Perform matrix multiplication
        result = np.matmul(arr_a, arr_b)
    except ValueError as e:
        raise ValueError("Matrices are not aligned for multiplication") from e

    # Convert result back to list of lists
    return result.tolist()
