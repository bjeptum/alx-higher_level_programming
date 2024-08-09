#!/usr/bin/python3
""" Print text Module with additional new lines """


def text_indentation(text):
    """Print text with 2 new lines after characters: ., ?, and :.

    Args:
        text (str): The text to be printed.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    while i < len(text):
        if text[i] in '.?:':
            print(text[i].strip())
            print()
            i += 1
            while i < len(text) and text[i] == ' ':
                i += 1
            continue
        print(text[i], end='')
        i += 1
    print()
