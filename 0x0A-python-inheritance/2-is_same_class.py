#!/usr/bin/python3
"""Module contains func is_kind_of_class"""


def is_kind_of_class(obj, a_class):
    """returns true if obj is of same class else, False"""
    return type(obj) == a_class
