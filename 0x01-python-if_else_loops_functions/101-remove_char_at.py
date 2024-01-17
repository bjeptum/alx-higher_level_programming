#!/usr/bin/python3
"""
Removes a character at position n
"""


def remove_char_at(str, n):
    sz = len(str)
    if (sz > n >= 0):
        return (str[:n] + str[n+1:])
    else:
        return (str)
