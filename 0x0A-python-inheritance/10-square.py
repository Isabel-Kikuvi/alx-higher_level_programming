#!/usr/bin/python3
"""Module contains a class BaseGeometry"""


class BaseGeometry:
    """contains public attribute area, integer_validator"""
    def area(self):
        """raises an exception when called"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):

    """Representation of a rectangle"""

    def __init__(self, width, height):
        """intantiates a rectangle"""
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """calculate the area"""
        return (self.__width * self.__height)

    def __str__(self):
        """declaring the print"""
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))


class Square(Rectangle):
    """the square module"""

    def __init__(self, size):
        """instantiates a square"""
        self.integer_validator('size', size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """"returns the area of the square"""
        return self.__size ** 2
