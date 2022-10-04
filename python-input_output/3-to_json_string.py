#!/usr/bin/python3
"""JSON representation of an object (string)"""
import json
"""json module"""


def to_json_string(my_obj):
    """JSON representation of an object (string)"""

    a = json.dumps(my_obj)
    return a
