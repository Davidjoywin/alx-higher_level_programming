#!/usr/bin/python3
"""Integers representing the pascal triangle"""


def pascal_triangle(n):
    """
    function: pascal_triangle
    n: height of the triangle
    Returns: list representing pascal triangle of n
    """
    outer_list = []
    inner_list = []
    if n <= 0:
        return outer_list

    for i in range(1, n+1):
        if i < 3:
            inner_list.append(1)
            outer_list.append(inner_list)
            inner_list = list(inner_list)
        else:
            temp = list()
            temp.append(1)
            list_len = len(inner_list)-1
            for j in range(list_len):
                if j < list_len:
                    temp.append(inner_list[j] + inner_list[j+1])
            temp.append(1)
            inner_list = list(temp)
            outer_list.append(inner_list)

    return outer_list
