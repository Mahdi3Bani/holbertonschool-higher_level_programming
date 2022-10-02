#!/usr/bin/python3
def read_file(filename=""):
    "function to print file"
    with open('filename', encoding="utf-8") as f:
        p = f.read()
    print(p)
