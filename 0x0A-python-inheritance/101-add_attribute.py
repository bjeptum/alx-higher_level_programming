#!/usr/bin/python3
"""
add_attribute Module
"""


def add_attribute(obj, attr, val):
    """Adds a new attribute to the object"""
    if not hasattr(obj, "__slots__") and not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    if hasattr(obj, "__slots__") and not hasattr(obj, attr):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, val)
