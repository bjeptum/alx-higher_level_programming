#!/usr/bin/python3
"""
Adds 2 tuples
"""


def add_tuple(tuple_a=(), tuple_b=()):
    a = tuple_a[:2] + (0, 0)[:2 - len(tuple_a)]
    b = tuple_b[:2] + (0, 0)[:2 - len(tuple_b)]
    tuple_c = tuple(map(lambda i, j: i + j, a, b))
    return tuple_c
