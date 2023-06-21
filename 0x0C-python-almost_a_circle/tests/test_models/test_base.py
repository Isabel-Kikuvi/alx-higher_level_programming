#!/usr/bin/python3
import unittest
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle
import json
import inspect

"""Creating test cases for the module Base"""


class test_base(unittest.TestCase):
    """Testing the class base"""
    def test_id_is_none(self):
        """Testing if id is not provided"""
        b = Base()
        self.assertEqual(1, b.id)
        b = Base()
        self.assertEqual(2, b.id)

    def test_id_input(self):
        """testing id input"""
        b = Base(89)
        self.assertEqual(89, b.id)

    def test_to_json_string(self):
        """testing json string"""
        s = Square(1)
        json_dict = s.to_dictionary()
        json_string = Base.to_json_string([json_dict])
        self.assertEqual(type(json_string), str)
    
    def test_to_json_isNone(self):
        """testing json string is none"""
        s = Square(5, 0, 0, 500)
        json_dict = s.to_dictionary()
        json_string = Base.to_json_string(None)
        self.assertEqual(json_string, "[]")

    def test_to_json_is_empty(self):
        """testing json string with []"""
        s = Square(5, 0, 0, 500)
        json_dict = s.to_dictionary()
        json_string = Base.to_json_string([])
        self.assertEqual(json_string, "[]")
    
    def test_to_json_value(self):
        """testing json string with value"""
        s = Square(5, 0, 0, 500)
        json_dict = s.to_dictionary()
        json_string = Base.to_json_string(json_dict)
        self.assertEqual(json.loads(json_string),
                         {"id": 500, "size": 5, "x": 0, "y": 0})
    
    def test_to_json_isNone(self):
        """testing json string is none in rectangle"""
        r = Rectangle(5, 1, 0, 0, 500)
        json_dict = r.to_dictionary()
        json_string = Base.to_json_string(None)
        self.assertEqual(json_string, "[]")

    def test_to_json_is_empty(self):
        """testing json string with [] in rectangle"""
        r = Rectangle(5, 1, 0, 0, 500)
        json_dict = r.to_dictionary()
        json_string = Base.to_json_string([])
        self.assertEqual(json_string, "[]")

    def test_to_json_value(self):
        """testing json string with value in rectangle"""
        r = Rectangle(5, 1, 0, 0, 500)
        json_dict = r.to_dictionary()
        json_string = Base.to_json_string(json_dict)
        self.assertEqual(json.loads(json_string),
                {"id": 500, "width": 5, "height": 1, "x": 0, "y": 0})
