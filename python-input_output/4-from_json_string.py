#!/usr/bin/python3
"""returns an object (Python data structure) represented by a JSON string)"""
import json
"""json module"""


def from_json_string(my_str):
    """returns an object (Python data structure) represented by a JSON string"""

    a = json.loads(my_str)
    return a
