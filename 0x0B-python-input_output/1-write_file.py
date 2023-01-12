#!/usr/bin/python3
"""writes a string to a test file(UTF8)"""


def write_file(filename="", text=""):
    """
    function: write_file
    filename: file to open
    text: string to write into the file
    Returns: None
    """
    with open(filename, 'w', encoding="utf-8") as file:
        return file.write(text)
