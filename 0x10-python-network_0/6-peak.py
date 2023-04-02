#!/usr/bin/python3
"""contains the function find_peak"""


def find_peak(list_of_integers):
    """finds a peak in a list of unsorted integers"""
    int_list = list_of_integers
    int_list_len = len(int_list)
    if int_list_len == 0:
        return
    m = int_list_len // 2
    if (m == int_list_len - 1 or int_list[m] >= int_list[m + 1]) \
            and (m == 0 or int_list[m] >= int_list[m - 1]):
        return int_list[m]
    if m != int_list_len - 1 and int_list[m + 1] > int_list[m]:
        return find_peak(int_list[m + 1:])
    return find_peak(int_list[:m])
