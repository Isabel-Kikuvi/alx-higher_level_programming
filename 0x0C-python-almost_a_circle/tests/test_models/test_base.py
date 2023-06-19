#!/usr/bin/python3
"""test the rectangle model"""
import unittest
from models.rectangle import Rectangle
from models.base import Base
import io
import sys


class test_Rectangle(unittest.TestCase):
    """Testing Rectangle"""
    def setUp(self):
        """Initializing instance width and height
            parameters"""
        self.r = Rectangle(5, 10)

    def tearDown(self):
        """Deleting created instance"""
        del self.r

    def test_height(self):
        """Testing height of rectangle"""
        self.assertEqual(10, self.r.height)

    def test_width(self):
        """Testing width of rectangle"""
        self.assertEqual(5, self.r.width)

    def test_x(self):
        """Testing x"""
        self.r.x = 60
        self.assertEqual(60, self.r.x)
        self.assertEqual(0, self.r.y)

    def test_y(self):
        """Testing y"""
        self.r.y = 55
        self.assertEqual(55, self.r.y)
        self.assertEqual(0, self.r.x)

    def test_id(self):
        """testing the id"""
        r = Rectangle(19, 23, 0, 0, 5)
        self.assertEqual(5, r.id)

    def test_width_str(self):
        """Testing if width input is str"""
        with self.assertRaises(TypeError):
            rect = Rectangle('1', 7)

if __name__ == "__main__":
    unittest.main()
