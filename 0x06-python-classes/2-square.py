#!/usr/bin/python3
"""
Defined Square Module
"""


class Square:
    "Define square with size"
    def __init__(self, size=0):
        " Class instantiator"
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        else:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
