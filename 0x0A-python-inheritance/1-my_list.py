#!/usr/bin/python3
"""
Modele: 1-my_list
"""


class MyList(list):
    """
    Class inherit from list
    """

    def print_sorted(self):
        """
        prints the list, but sorted (ascending sort)
        """
        print(sorted(self))
