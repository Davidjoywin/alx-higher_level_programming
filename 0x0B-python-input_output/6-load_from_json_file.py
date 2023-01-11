#!/usr/bin/python3
"""Creates an Object from a JSON file"""


json = __import__('json')
def load_from_json_file(filename):
    """
    function: load_from_json
    filename: file to load json from
    Returns: Object data
    """
    with open(filename, 'r') as file:
        get_obj = json.load(file)
        return get_obj
