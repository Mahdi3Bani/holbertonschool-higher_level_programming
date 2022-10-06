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

    @staticmethod
    def to_json_string(list_dictionaries):
        """"to json string"""
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        ''''save to file'''
        obj = []
        with open(cls.__name__ + ".json", 'w') as f:
            if list_objs is None:
                json.dumps(obj, f)
            else:
                for i in list_objs:
                    obj.append(i.to_dictionary())
                f.write(cls.to_json_string(obj))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if json_string is None:
            return []
        else:
            return json.loads(json_string)
