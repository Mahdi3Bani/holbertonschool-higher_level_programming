#!/usr/bin/python3
""" class Rectangle that inherits from Base"""

from turtle import width
from models.base import Base


class Rectangle(Base):
    """"class Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """"Class constructor"""
        id = super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        ''''return the area of triangle'''
        return self.__height * self.__width

    def display(self):
        """"display triangle"""
        for l in range(self.__y):
            print()
        for i in range(self.__height):
            for j in range(self.__width + self.__x):
                if j < self.__x:
                    print(" ", end="")
                    continue
                print("#", end="")
            print()

    def __str__(self):
        """"print"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args):
        """"assigns an argument to each attribute"""

        up = ["id", "width", "height", "x", "y"]
        if len(args) != 0:
            for i in range(len(args)):
                setattr(self, up[i], args[i])
