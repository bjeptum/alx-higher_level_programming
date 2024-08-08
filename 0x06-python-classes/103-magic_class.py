#!/usr/bin/python3
"""
Defined MagicClass
Includes methods to calculate area and circumference
of a circle given a radius.
"""
import math


class MagicClass:
    """
    Class to represent a circle and compute its area and circumference.
    """
    def __init__(self, radius=0):
        """
        Initialization of MagicClass with a given radius.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """
        Calculate the area of the circle.
        """
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        """
        Calculate the circumference of the circle.
        """
        return 2 * math.pi * self.__radius
