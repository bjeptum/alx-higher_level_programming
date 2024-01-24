#!/usr/bin/python3
"""
Prints a dictionary by ordered keys
"""


def print_sorted_dictionary(a_dictionary):
    new_list = sorted(a_dictionary.items())
    new_dict = {}
    for k, v in new_list:
        new_dict[k] = v

    print(new_dict)
