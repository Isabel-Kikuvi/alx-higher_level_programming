#!/usr/bin/python3

"""Defines class Square"""


class Square:
    """Reps a square"""
    def __init__(self, size=0):
        """Initializes a square.
        Args:
        size (int): Size of square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
