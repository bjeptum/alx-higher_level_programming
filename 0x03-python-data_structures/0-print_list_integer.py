#!/usr/bin/python3
"""
Prints all integers of a list
"""


def print_list_integer(my_list=[]):
    for num in my_list:
        print("{:d}".format(num), sep="\n")
