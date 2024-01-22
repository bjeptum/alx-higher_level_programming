#!/usr/bin/python3
"""
Prints all integers of a list
In reverse order
"""


def print_reversed_list_integer(my_list=[]):
    new_list = my_list[::-1]
    for num in new_list:
        print("{:d}".format(num), sep="\n")
