#!/usr/bin/python3
"""Module contains read_file"""


def read_file(filename=""):
    """reads a file with utf-8"""
    with open(filename, encoding='utf-8') as f:
        print(f.read(), end="")
