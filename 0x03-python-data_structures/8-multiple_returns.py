#!/usr/bin/python3
"""
Returns a tuple with the length
Of a string and its first character
"""


def multiple_returns(sentence):
    length = len(sentence)
    if length != 0:
        return (length, sentence[0])
    else:
        return (0, None)
