#!/usr/bin/python3
"""" class"""


from curses.textpad import rectangle


class Rectangle:
    """"Rectangle class """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        hash = ""
        if self.width == 0 or self.height == 0:
            return hash
        for i in range(self.height):
            for j in range(self.width):
                if type(self.print_symbol) in [list, tuple, dict, int]:
                    hash += repr(self.print_symbol)
                else:
                    hash += self.print_symbol
            hash += "\n"
        return hash[0:len(hash) - 1]

    def __repr__(self):
        return "Rectangle(" + str(self.width) + ", " + str(self.height) + ")"

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

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


    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_1 >= rect_2:
            return rect_1
        else:
            return rect_2
