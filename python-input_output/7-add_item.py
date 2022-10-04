#!/usr/bin/python3
""""adds all arguments to a Python list"""
import sys


save_to_json_file = __import__('save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

open("add_item.json", 'a')
try:
    a = load_from_json_file("add_item.json")
except ValueError:
    a = []
save_to_json_file(a + sys.argv[1:], "add_item.json")
