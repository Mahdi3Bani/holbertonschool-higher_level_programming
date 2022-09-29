#!/usr/bin/python3
""""square class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """"square"""

    def __init__(self, size):
        """Intialize a new instance from Square
        Args:
            size (int):The size of The new Square
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Intialize a new instance from Square"""
        return self.__size ** 2
