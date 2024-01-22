#!/usr/bin/python3
"""
Retrieves an element from a list
"""


def element_at(my_list, idx):
    length = len(my_list)
    elem = my_list[idx]
    if idx < 0:
        return None
    elif idx > length:
        return None
    else:
        return elem
