#!/usr/bin/python3
def safe_print_integer_err(value):
	sys = __import__('sys')
	try:
		print("{:d}".format(value))
		return True
	except ValueError:
		sys.stderr.write(value)
		return False

safe_print_integer_err("hello")
print(safe_print_integer_err("hello"))
