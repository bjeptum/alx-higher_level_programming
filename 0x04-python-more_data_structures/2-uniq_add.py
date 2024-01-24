#!/usr/bin/python3
"""
Add all unique integers
in alist
"""


def uniq_add(my_list=[]):
    new_list = set(my_list)
    return sum(new_list)
