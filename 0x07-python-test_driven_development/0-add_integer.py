#!/usr/bin/python3

def add_integer(a, b=98):
    """
    Adds two integers and returns the result
    """
    if isinstance(a, float) or isinstance(b, float):
        a = int(a)
        b = int(b)

    if not isinstance(a, int):
        raise TypeError("a must be an integer")
    elif not isinstance(b, int):
        raise TypeError("b must be an integer")
    else:
        return a + b
