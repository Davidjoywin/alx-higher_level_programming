#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
	result = 0
	new_list = []

	if len(my_list_1) != len(my_list_2):
		print("out of range")

	for i in range(list_length):
		try:
			result = my_list_1[i] / my_list_2[i]
			new_list.append(result)

		except ZeroDivisionError:
			print("division by 0")

		except TypeError:
			print("wrong type")

		except IndexError:
			break

	return new_list

my_list_1 = [3,2,2]
my_list_2 = [4,5,4,3]
print(list_division(my_list_1, my_list_2, 4))
