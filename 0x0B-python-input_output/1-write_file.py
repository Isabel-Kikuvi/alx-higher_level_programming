#!/usr/bin/python3
"""Module contains write_file"""


def write_file(filename="", text=""):
    """writes string to text file"""
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
