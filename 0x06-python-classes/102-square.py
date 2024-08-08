#!/usr/bin/python3
"""
Defined Square Module
"""


class Square:
    """
    Define a square with attribute size,
    with methods to retrieve and set size.
    """
    def __init__(self, size=0):
        """
        Initialize a new Square instance with a given size.
        """
        self.size = size

    @property
    def size(self):
        """
        Getter method for the size attribute.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method for the size attribute.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates the area of the square.
        """
        return self.__size ** 2

    def __eq__(self, other):
        """
        Compare if two Square instances have equal areas.
        """
        if isinstance(other, Square):
            return self.area() == other.area()
        return False

    def __ne__(self, other):
        """
        Compare if two Square instances have different areas.
        """
        if isinstance(other, Square):
            return self.area() != other.area()
        return False

    def __gt__(self, other):
        """
        Compare if the area of the current Square is greater than
        that of another Square.
        """
        if isinstance(other, Square):
            return self.area() > other.area()
        return NotImplemented

    def __ge__(self, other):
        """
        Compare if the area of the current Square is greater than
        or equal to that of another Square.
        """
        if isinstance(other, Square):
            return self.area() >= other.area()
        return NotImplemented

    def __lt__(self, other):
        """
        Compare if the area of the current Square is less than
        that of another Square.
        """
        if isinstance(other, Square):
            return self.area() < other.area()
        return NotImplemented

    def __le__(self, other):
        """
        Compare if the area of the current Square is less than
        or equal to that of another Square.
        """
        if isinstance(other, Square):
            return self.area() <= other.area()
        return NotImplemented
