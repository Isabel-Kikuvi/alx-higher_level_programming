#!/usr/bin/python3
"""Module contains class Student"""


class Student:
    """represents a student"""
    def __init__(self, first_name, last_name, age):
        """initiates the class student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retreives dict rep of student"""
        if attrs is None:
            return self.__dict__

        new_dict = {}
        for a in attrs:
            try:
                new_dict[a] = self.__dict__[a]

        return new_dict
