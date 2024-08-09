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
    # Characters that trigger new lines
    nw_chars = {'.', '?', ':'}

    i = 0
    while i < len(text):
        # Print the current character
        print(text[i], end="")

        # Check if the current character trigger new
        if text[i] in nw_chars:
            # Print two new lines after the trigger character
            print()
            print()

            # Skip any subsequent spaces
            i += 1
            while i < len(text) and text[i] == ' ':
                i += 1
            continue

        i += 1

    # Ensure a final new line at the end if text ends with a trigger character
    if text and text[-1] in nw_chars:
        print()
