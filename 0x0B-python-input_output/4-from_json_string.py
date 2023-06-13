#!/usr/bin/python3
"""MOdule contains from_pjson_string"""


import json


def from_json_string(my_str):
    """returns an obj represented by json my_str"""
    return json.loads(my_str)
