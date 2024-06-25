#!/usr/bin/python3
"""
Defined Square Module
"""


class Square:
    """
    Define square with attribute size
    with methods to retrieve and set size
    """
    def __init__(self, size=0):
        " Class instantiator"
        self.size = size

    @property
    def size(self):
        " Getter method for size attribute"
        return self.__size

    @size.setter
    def size(self, value):
        " Setter method for size attribute"
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value

    def area(self):
        " Calculates area of square"
        return self.__size ** 2
