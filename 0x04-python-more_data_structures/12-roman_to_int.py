#!/usr/bin/python3
"""
Converts Roman numeral to integer
"""


def roman_to_int(roman_string):
    roman_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
            'IV': 4,
            'IX': 9,
            'XL': 40,
            'XC': 90,
            'CD': 400,
            'CM': 900
            }
    if type(roman_string) is not str or roman_string is None:
        return 0
    i = 0
    num = 0
    while i < len(roman_string):
        if i + 1 < len(roman_string) and roman_string[i:i + 2] in roman_dict:
            num += roman_dict[roman_string[i: i + 2]]
            i += 2
        else:
            num += roman_dict[roman_string[i]]
            i += 1
    return num
