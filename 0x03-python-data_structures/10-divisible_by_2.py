#!/usr/bin/python3
"""
Finds all multiples of 2 in a list
"""


def divisible_by_2(my_list=[]):
    new_list = my_list.copy()
    ans = []
    for num in new_list:
        if num % 2 == 0:
            ans.append(True)
        else:
            ans.append(False)
    return ans
