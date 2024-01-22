#!/usr/bin/python3
"""
Removes all characters c and C from
a string
"""


def no_c(my_string):
    new_str = list(my_string)
    new_str = [char for char in new_str if char.lower() not in ('c', 'C')]
    return ''.join(new_str)
