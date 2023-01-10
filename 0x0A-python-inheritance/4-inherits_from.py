#!/usr/bin/python3
"""
module: 4-inherits_from
"""


def inherits_from(obj, a_class):
    """
    The obj is an instance of a class that inherit (directly or indirectly)
    obj: an object
    a_class: a class
    Returns: None
    """
    return type(obj) != a_class and isinstance(obj, a_class)
