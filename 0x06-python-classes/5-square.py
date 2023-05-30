#!/usr/bin/python3

"""Defines a class Square"""


class Square:
    """Reps a class Square"""
    def __init__(self, size=0):
        """Initializes class square.
        Args:
        size (int): size of square.
        """
        self.__size = size

    @property
    def size(self):
        """Sets size of the square"""
        return self.__size
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns Area of a square"""
        return self.__size ** 2
    def my_print(self):
        """Prints square with #"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
