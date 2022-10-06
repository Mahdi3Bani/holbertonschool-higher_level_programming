#!/usr/bin/python3
""""class base"""


import json


class Base:
    ''''class base'''

    __nb_objects = 0

    def __init__(self, id=None):
        """"class constructor"""

        if id is None:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
        else:
            self.id = id