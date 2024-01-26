#!/usr/bin/python3
"""
Deleted a key in a dictionary
"""


def simple_delete(a_dictionary, key=""):
    if key in a_dictionary:
        try:
            del a_dictionary[key]
        except KeyError:
            pass
    return a_dictionary


def print_sorted_dictionary(a_dictionary):
    new_dict = sorted(a_dictionary.items())
    for k, v in new_dict:
        print(f"{k}: {v}")
