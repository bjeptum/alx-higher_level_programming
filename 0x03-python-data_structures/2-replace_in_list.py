#!/usr/bin/python3
"""
Replaces an element of a list at
a specific position(like in C)
"""


def replace_in_list(my_list, idx, element):
    length = len(my_list)
    if idx < 0 or idx >= length:
        return my_list
    else:
        my_list[idx] = element
        return my_list
