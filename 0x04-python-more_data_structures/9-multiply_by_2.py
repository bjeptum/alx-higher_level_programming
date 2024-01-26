#!/usr/bin/python3
"""
Returns a new dictionary
with all values multiplied by 2
"""


def multiply_by_2(a_dictionary):
    new_dict = {key: value * 2 for key, value in a_dictionary.items()}
    return new_dict


def print_sorted_dictionary(a_dictionary):
    new_dict = sorted(a_dictionary.items())
    for k, v in new_dict:
        print(f"{k}: {v}")
