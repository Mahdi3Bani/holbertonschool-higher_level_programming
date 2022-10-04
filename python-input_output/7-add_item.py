#!/usr/bin/python3
""""adds all arguments to a Python list"""

import sys

if __name__ == "__main__":
    save_to_json_file = __import__('save_to_json_file').save_to_json_file
    load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

    name = "add_item.json"
    arg = sys.argv[1:]
    try:
        a = load_from_json_file("add_item.json")
    except ValueError:
        a = []

    a.append(arg)
    save_to_json_file(a, name)
