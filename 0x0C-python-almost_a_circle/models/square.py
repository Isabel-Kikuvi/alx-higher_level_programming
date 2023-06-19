#!/usr/bin/python3
"""A representation of the class Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Initializes a Square"""
    def __init__(self, size, x=0, y=0, id=None):
        """Class constructor"""
        super().__init__(width=size, height=size, x=x, y=y, id=id)

    def __str__(self):
        """Prints a statement when called"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.width)

    @property
    def size(self):
        """ size getter"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """updates arguments"""
        if args:
            num_args = len(args)
            if num_args >= 1:
                self.id = args[0]
            if num_args >= 2:
                self.size = args[1]
            if num_args >= 3:
                self.x = args[2]
            if num_args >= 4:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """return the dict rep of attr"""
        return {'id': self.id,
                'size': self.size,
                'x': self.x,
                'y': self.y}
