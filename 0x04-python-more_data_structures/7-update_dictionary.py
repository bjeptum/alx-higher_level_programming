#!/usr/bin/python3
"""
Replaces or adds key/value
In a dictionary
"""


def update_dictionary(a_dictionary, key, value):
    a_dictionary[key] = value
    return a_dictionary


def print_sorted_dictionary(a_dictionary):
    new_dict = sorted(a_dictionary.items())
    for k, v in new_dict:
        print(f"{k}: {v}")
