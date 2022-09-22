#!/usr/bin/python3
"""" class"""


from turtle import width


class Rectangle:
    """"Rectangle class """

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def __str__(self):
        hash = ""
        if self.width == 0 or self.height == 0:
            return hash
        for i in range(self.height):
            for j in range(self.width):
                hash = hash + "#"
            hash += "\n"
        return hash[0:len(hash) - 1]
    
    def __repr__(self):
        return "Rectangle(" + str(self.width) + "," + str(self.height) + ")"

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__height + self.__width) * 2
