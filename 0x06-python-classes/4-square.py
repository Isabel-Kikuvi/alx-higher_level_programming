#!/usr/bin/python3

"""Defines class Square"""


class Square:
    """Reps a square"""
    def __init__(self, size=0):
        """Initializes a class square
        Args:
        size (int): size of square.
        """
        self.size = size

    @property
    def size(self):
        """Gets size of square"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the area of a square"""
        return self.__size ** 2
