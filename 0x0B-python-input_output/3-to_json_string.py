#!/usr/bin/python3
"""JSON representation of an object"""
dumps = __import__('json').dumps

def to_json_string(my_obj):
    """
    function: to_json_string
    my_obj: json obj representation
    Returns: json object
    """
    obj = dumps(my_obj)
    return obj
