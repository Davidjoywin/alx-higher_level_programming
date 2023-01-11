#!/usr/bin/python3
"""Dictionary description with simple data structurn"""


def class_to_json(obj):
    """
    function: class_to_json
	obj: object to get its dict representation
    Returns: Dictionary representation
	"""
    return obj.__dict__
