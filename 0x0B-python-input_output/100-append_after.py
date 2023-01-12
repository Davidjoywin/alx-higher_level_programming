#!/usr/bin/python3
"""Insert after a line of text to a file"""


def append_after(filename="", search_string="", new_string=""):
    """
    function: append_after
    filename: filename to read
    search_string: string to search for
    new_string: string to be inserted into the file
    """

    new_list = []
    with open(filename, 'r', encoding='utf-8') as file:
        get_file = file.read()

        text_list = get_file.split("\n")
        for text in text_list:
            new_list.append(text)
            if search_string in text:
                new_string = new_string.strip('\n')
                new_list.append(new_string)
        new_list = "\n".join(new_list)

    with open(filename, 'w', encoding='utf-8') as file:
        file.write(new_list)
