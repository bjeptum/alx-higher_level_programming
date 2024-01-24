#!/usr/bin/python3
"""
Prints a dictionary by ordered keys
"""


def print_sorted_dictionary(a_dictionary):
    new_dict = sorted(a_dictionary.items())
    for k, v in new_dict:
        print(f"{k}: {v}")
