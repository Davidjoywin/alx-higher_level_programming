#!/usr/bin/python3
"""Object to a text file"""


json = __import__('json')
def save_to_json_file(my_obj, filename):
    """
    function: save_to_json_file
    my_obj: object data type to save
    filename: where to save my_obj
    """
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
