#!/usr/bin/python3
"""
Defined Square Module
"""


class Square:
    """
    Define square with attributes size and position,
    with methods to retrieve and set these attributes.
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new Square instance.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Getter method for size attribute.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method for size attribute.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Getter method for position attribute.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter method for position attribute.
        """
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
        """
        Calculates the area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square with # characters.
        """
        if self.__size == 0:
            print("")
        else:
            for _ in range(self.__position[1]):
                print("")
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """
        Returns the string representation of the square.
        """
        output = []
        if self.__size == 0:
            return ""
        else:
            for _ in range(self.__position[1]):
                output.append("")
            for _ in range(self.__size):
                output.append(" " * self.__position[0] + "#" * self.__size)
            return "\n".join(output)
