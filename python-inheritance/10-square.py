#!/usr/bin/python3
""""square class"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle.py').Rectangle


class Square(Rectangle):
    """"square"""

    def __init__(self, size):
        """"initialization"""

        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """"implementation"""
        return self.__size ** 2
