#!/usr/bin/python3
"""
2-is_same_class module
"""


def is_same_class(obj, a_class):
    """Checks if an object is an instance of specified class"""
    return(type(obj) is a_class)
