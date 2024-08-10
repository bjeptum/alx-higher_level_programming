#!/usr/bin/python3
"""
Rectangle module
Defined with attributes
With Area and Perimeter defined
"""


class Rectangle:
    " Complete definition of a rectangle"

    def __init__(self, width=0, height=0):
        "Class instantiation"
        self.width = width
        self.height = height

    @property
    def width(self):
        "Getter method for width attribute"
        return self.__width

    @width.setter
    def width(self, value):
        "Setter method for width attribute"
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        "Getter method for height attribute"
        return self.__height

    @height.setter
    def height(self, value):
        "Setter methodfor height attribute"
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        "Calculates area of rectangle"
        arr = self.__width * self.__height
        return arr

    def perimeter(self):
        "Calculates perimeter of rectangle"
        if (self.__width == 0 or self.__height == 0):
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        "Returns a string representation of the rectangle"
        if self.__width == 0 or self.__height == 0:
            return ""
        return '\n'.join('#' * self.__width for _ in range(self.__height))

    def __repr__(self):
        "Returns a string representation of the rectangle"
        return f"Rectangle({self.__width}, {self.__height})"
