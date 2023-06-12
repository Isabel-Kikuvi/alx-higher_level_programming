#!/usr/bin/python3
"""Module contains the func inherits_from"""


def inherits_from(obj, a_class):
    """returns True if obj is a sub_class of a_class, else False"""
    return issubclass(type(obj), a_class) and type(obj) != a_class
