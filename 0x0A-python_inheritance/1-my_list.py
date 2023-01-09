#!/usr/bin/python3

class MyList(list):
	"""
	Class inherit from list
	"""
	def print_sorted(self):
		"""
		prints the list, but sorted (ascending sort)
		"""
		return sorted(self)
