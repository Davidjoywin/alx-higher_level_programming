#!/usr/bin/python3
"""Object(Python data structure) representd by a JSON string"""


loads = __import__('json').loads
def from_json_string(my_str):
    """
    function: from_json_string
    my_str: JSON string
	Returns: an object
    """
    obj = loads(my_str)
    return obj
