#!/usr/bin/python3
"""
Computes a power b
"""


def pow(a, b):
    while b != 0:
        if b == 1:
            return a
        elif b < 0:
            return (1 / pow(a, -b))
        else:
            for i in range(b):
                return (a * pow(a, b-1))
        break
    return 1
