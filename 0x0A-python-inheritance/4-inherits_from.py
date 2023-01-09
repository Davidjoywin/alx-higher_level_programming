#!/usr/bin/python3

def inherits_from(obj, a_class):
	"""
	The obj is an instance of a class that inherit (directly or indirectly)
	"""
	return type(obj) != a_class and isinstance(obj, a_class)
