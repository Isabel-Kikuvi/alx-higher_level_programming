#!/usr/bin/python3
"""Contains MyList Class """


class MyList(list):
    """Subclass of class list"""
    def __init__(self):
        """initializes the object"""
        super().__init__()

    def print_sorted(self):
        """prints a sorted list"""
        sorted_list = sorted(self)
        print(sorted_list)
