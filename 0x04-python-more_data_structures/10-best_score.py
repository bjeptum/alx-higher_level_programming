#!/usr/bin/python3
"""
Return a key with the biggest integer value
"""


def best_score(a_dictionary):
    if not a_dictionary:
        return None
    large = max(a_dictionary.values())
    ans = [key for key in a_dictionary if a_dictionary[key] == large]
    if ans:
        return ans[0]
    else:
        return None
