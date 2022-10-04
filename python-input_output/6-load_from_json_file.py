#!/usr/bin/python3
"""writes an Object to a text file"""
import json
"""json module"""


def load_from_json_file(filename):
    """writes an Object to a text file"""

    with open(filename, mode='w', encoding="utf-8") as f:
        json.load(filename)
