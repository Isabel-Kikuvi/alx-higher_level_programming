#!/usr/bin/python3
"""Module contains save_to_json_file"""


import json


def save_to_json_file(my_obj, filename):
    """loads an object to json"""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
