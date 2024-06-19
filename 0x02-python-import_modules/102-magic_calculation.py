#!/usr/bin/python3
import magic_calculation_102
from magic_calculation_102 import add, sub


def magic_calculation(a, b):
    if a < b:
        return add(a, b)
    elif a > b:
        c = sub(a, b)
        if c < 4:
            return 0
        else:
            return add(c, 10)
    else:
        return a * b
