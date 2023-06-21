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
            r = Rectangle('1', 7)

    def test_height_str(self):
        """Testing if height input is str"""
        with self.assertRaises(TypeError):
            r = Rectangle(1, '7')

    def test_width_zero(self):
        """Testing if width input is zero"""
        with self.assertRaises(ValueError):
            r = Rectangle(0, 7)

    def test_height_zero(self):
        """Testing if height input is zero"""
        with self.assertRaises(ValueError):
            r = Rectangle(1, 0)

    def test_x_negative(self):
        """Testing if x value is negative"""
        with self.assertRaises(ValueError):
            r = Rectangle(1, 7, -1, 5)

    def test_y_negative(self):
        """Testing if y value is negative"""
        with self.assertRaises(ValueError):
            r = Rectangle(1, 7, 1, -5)

    def test_width_negative(self):
        """Testing a negative width input"""
        with self.assertRaises(ValueError):
            r = Rectangle(-1, 7)

    def test_height_negative(self):
        """Testing a negative height input"""
        with self.assertRaises(ValueError):
            r = Rectangle(1, -7)
    
    def test_x_str(self):
        """Testing an str value for x"""
        with self.assertRaises(TypeError):
            r = Rectangle(1, 7, '1', 5)

    def test_y_str(self):
        """Testing an str value for y"""
        with self.assertRaises(TypeError):
            r = Rectangle(1, 7, 1, '5')

    def test_str(self):
        """Testing str """
        r = Rectangle(1, 7, 1, 5, 89)
        self.assertEqual(r.__str__(), "[Rectangle] (89) 1/5 - 1/7")

    def test_area(self):
        """testing the area"""
        r = Rectangle(2, 10)
        self.assertEqual(20, r.area())

    def test_area_5args(self):
        """testing area with all 5 args"""
        r = Rectangle(2, 10, 4, 5, 17)
        self.assertEqual(20, r.area())

if __name__ == "__main__":
    unittest.main
