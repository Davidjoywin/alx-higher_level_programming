#!/usr/bin/python3
"""Student that defines a student"""


class Student:
    """Student class"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

	def to_json(self, attrs=None):
		if attrs:
            result_attr = dict()
            for attr in attrs:
                try:
                    result_attr[attr] = self.__dict__[attr]
                except Exception:
                    continue
			return result_attr
        return self.__dict__

def reload_from_json(self, json):
	pass
