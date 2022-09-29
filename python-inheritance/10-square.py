#!/usr/bin/python3
""""square class"""


Rectangle = __import__('9-rectangle.py').Rectangle


class Square(Rectangle):
    """"square"""

    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        return self.__size ** 2
