#!/usr/bin/python3
"""
Defines a class-checking functon.
"""

def is_same_class(obj, a_class):
	"""
	function that returns True if the object is exactly an instance 
	specified class; otherwise False
	"""
	return type(obj) == a_class
