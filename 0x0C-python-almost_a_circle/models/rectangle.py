#!/usr/bin/python3
"""Representation of classRectagle which inherits from Base"""
from models.base import Base


class Rectangle(Base):
    """initiatizes a rectagle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Class constructor"""
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """gets the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the width"""
        if type(value) !=  int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """gets the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the height"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """gets x"""
        return self.__x

    @x.setter
    def x(self, value):
        """sets x"""
        if type(x) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")

    @property
    def y(self):
        """gets y"""
        return self.__y

    @y.setter
    def y(self, value):
        """sets y"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")

    def area(self):
        """calculates the area of a square"""
        return self.__height * self.__width

    def display(self):
        """Printa a rectangle to stdout using #"""
        if self.__height == 0 or self.__width == 0:
            print("")
            return
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print("" * self.__x + "#" * self.__width)

    def __str__(self):
        """Print a statement"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.__x,
                                                       self.__y,
                                                       self.__width,
                                                       self.__height)

    def update(self, *args, **kwargs):
        """updates arguments"""
        if args:
            num_args = len(args)
            if num_args >= 1:
                self.id = args[0]
            if num_args >= 2:
                self.__width = args[1]
            if num_args >= 3:
                self.__height = args[2]
            if num_args >= 4:
                self.__x = args[3]
            if num_args >= 5:
                self.__y = args[4]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = value
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value
                else:
                    raise ValueError("Invalid attribut: {key}")

    def to_dictionary(self):
        """Returns the dict representation of a rectagle"""
        return {'id': self.id,
                'width': self.width,
                'height': self.height,
                'x': self.x,
                'y': self.y}
