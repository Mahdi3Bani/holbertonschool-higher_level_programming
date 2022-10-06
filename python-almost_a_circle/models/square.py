#!/usr/bin/python3
""" class square that inherits from Base"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """"sqaure class"""

    def __init__(self, size, x=0, y=0, id=None):
        """ square class"""

        super().__init__(size, size, x, y, id)
        self.width = size
        self.height = size

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value

    def __str__(self):
        """print the str of Rectangle"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)
