#!/usr/bin/python3
"""
Full rectangle module
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle subclass"""
    def __init__(self, width, height):
        """Instantiation method"""
        self.__width = width
        self.__height = height
        super(Rectangle, self).integer_validator('width', self.__width)
        super(Rectangle, self).integer_validator('height', self.__height)

    def area(self):
        """Calculates area"""
        return self.__width * self.__height

    def __str__(self):
        """Returns a rectangle description"""
        return "[Rectangle]" + str(self.__width) + "/" + str(self.__height)
