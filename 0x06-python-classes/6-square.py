#!/usr/bin/python3
"""
Defined Square Module
"""


class Square:
    """
    Define square with attribute size
    with methods to retrieve and set size
    """
    def __init__(self, size=0, position=(0, 0)):
        " Class instantiator"
        self.__size = size
        self.__position = position

    @property
    def size(self):
        " Getter method for size attribute"
        return self.__size

    @size.setter
    def size(self, value):
        " Setter method for size attribute"
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        " Getter method for position attribute"
        return self.__position

    @position.setter
    def position(self, value):
        " Setter method for position attribute"
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(val, int) for val in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        if any(val < 0 for val in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        " Calculates area of square"
        return self.__size ** 2

    def my_print(self):
        " Prints in stdout the square with #"
        if self.__size == 0:
            print("")
        else:
            for _ in range(self.__position[1]):
                print("")
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
