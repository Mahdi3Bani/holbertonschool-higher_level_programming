#!/usr/bin/python3
"function that writes a string to a text file"


def write_file(filename="", text=""):
    "function to write"
    with open(filename, mode='w', encoding="utf-8") as f:
        p = f.write(text)
    return p
