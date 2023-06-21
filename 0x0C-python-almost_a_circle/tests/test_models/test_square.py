#!/usr/bin/python3
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

"""Tests for class square"""


class test_square(unittest.TestCase):
    """testing the class square"""
    def setUp(self):
        """initiatizing instance with size parameter"""
        self.s = Square(7)

    def tearDown(self):
        """Deleting created instance"""
        del self.s

    def test_size(self):
        """testing the size arg"""
        self.assertEqual(7, self.s.size)

    def test_x(self):
        """testing x"""
        s = Square(7, 5)
        self.assertEqual(5, s.x)

    def test_y(self):
        """testing for y"""
        s = Square(7, 5, 10)
        self.assertEqual(10, s.y)

    def test_id(self):
        """testing for square id"""
        s = Square(7, 5, 10, 89)
        self.assertEqual(89, s.id)

    def test_size_str(self):
        """testing for str input for size"""
        with self.assertRaises(TypeError):
            s = Square("5")

    def test_size_negative(self):
        """testing for negative input in size"""
        with self.assertRaises(ValueError):
            s = Square(-5)

    def test_size_zero(self):
        """testing with size = 0"""
        with self.assertRaises(ValueError):
            s = Square(0)

    def test_x_str(self):
        """testing for str input for x"""
        with self.assertRaises(TypeError):
            s = Square(7, "5")

    def test_x_negative(self):
        """testing for negative input in x"""
        with self.assertRaises(ValueError):
            s = Square(7, -5)

    def test_y_str(self):
        """testing for str input for x"""
        with self.assertRaises(TypeError):
            s = Square(7, 5, "10")

    def test_y_negative(self):
        """testing for negative input in y"""
        with self.assertRaises(ValueError):
            s = Square(7, 5, -10)

    def test_str(self):
        """testing the __str__ method"""
        s = Square(7, 5, 10, 89)
        self.assertEqual("[Square] (89) 5/10 - 7", str(s))
