#!/usr/bin/python3
import unittest
from models.base import Base
from models.square import Square
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
        b = Base(89)
        self.assertEqual(89, b.id)

