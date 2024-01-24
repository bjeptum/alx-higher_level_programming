#!/usr/bin/python3
"""
Replaces all occurrences
of an element by another in a new list
"""
def search_replace(my_list, search, replace):
    new_list = list(map(lambda item: replace if item == search else item, my_list))
    return new_list
