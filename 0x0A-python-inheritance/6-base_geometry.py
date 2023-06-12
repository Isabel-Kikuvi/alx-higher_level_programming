#!/usr/bin/python3
"""Module contains the class BaseGeometry"""


class BaseGeometry:
    """contains public attribute area"""
    def area(self):
        """raises an exception when called"""
        raise Exception("area() is not implemented")
