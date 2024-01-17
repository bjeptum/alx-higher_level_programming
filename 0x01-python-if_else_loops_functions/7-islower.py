#!/usr/bin/python3
"""
Checks inputted char if lowercase
"""


def islower(c):
    char = ord(c)
    if (char >= 97 and char <= 123):
        return True
    else:
        return False
