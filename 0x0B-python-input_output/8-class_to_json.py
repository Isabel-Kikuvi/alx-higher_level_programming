#!/usr/bin/python3
"""Module contains class_to_json"""


def class_to_json(obj):
    """Returns dict desription of data"""
    return obj.__dict__
