#!/usr/bin/python3
"""
Retrieves an element from a list
"""


def element_at(my_list, idx):
    length = len(my_list)
    if idx < 0 or idx >= length:
        return None
    else:
        elem = my_list[idx]
        return elem
