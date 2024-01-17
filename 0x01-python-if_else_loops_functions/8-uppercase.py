#!/usr/bin/python3
"""
Prints inputted string in uppercase
"""


def uppercase(str):
    new_str = ""
    for char in str:
        c = ord(char)
        if (c >= 97 and c <= 123):
            new_str += chr(c - 32)
        else:
            new_str += char
    print(new_str)
