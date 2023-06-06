#!/usr/bin/python3
"""Defines a function that adds two ints"""


def add_integer(a, b=98):
    """Returns addition of two ints
    Args:
        a: (int/float) first number
        b: (int/float) second number initialized at 98
    Raises:
        TypeError if a or b are not float or int
    Returns:
        addition of two ints
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return int (a) + int (b)    
