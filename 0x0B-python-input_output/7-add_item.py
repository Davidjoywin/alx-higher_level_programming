#!/usr/bin/python3
"""Adds all arguments to a python list"""


sys = __import__('sys')
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
my_list = [i for i in sys.argv[1:]]
load_list = []

try:
    load_list = load_from_json_file("add_item.json")
except FileNotFoundError:
    pass
load_list.extend(my_list)
save_to_json_file(load_list, "add_item.json")
