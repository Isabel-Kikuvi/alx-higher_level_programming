#!/usr/bin/python3

"""Represents a class Base"""
import json


class Base:
    """Initializes a class Base"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Class constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns Json string"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes json string to file"""
        filename = cls.__name__ + ".json"
        with open(filename, "w") as f:
            if (list_objs is None or list_objs == []):
                f.write('[]')
            else:
                list_dict = [i.to_dictionary() for i in list_objs]
                f.write(Base.to_json_string(list_dict))

    @staticmethod
    def from_json_string(json_string):
        """returns a list from Json string"""
        if json_string is None or json_string == "[]":
            return "[]"
        else:
            return json.loads(json_string)
