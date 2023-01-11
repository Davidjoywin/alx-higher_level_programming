#!/usr/bin/python3
"""reads a text file(UTF8) and prints it to stdout"""


def read_file(filename=""):
    """
	function: read_file
	filename: file to read
	Returns: None
	"""
    with open(filename, 'r', encoding="utf-8") as file:
        get_file = file.read()
        print(get_file)
