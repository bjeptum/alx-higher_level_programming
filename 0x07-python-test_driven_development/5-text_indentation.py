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

    result = ""
    i = 0
    while i < len(text):
        if text[i] in '.?:':
            result += text[i]
            result += '\n\n'
            i += 1
            while i < len(text) and text[i] == ' ':
                i += 1
            continue
        result += text[i]
        i += 1

    # Strip leading/trailing spaces and ensure correct formatting
    print('\n'.join(line.strip() for line in result.splitlines()))
