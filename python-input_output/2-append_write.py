#!/usr/bin/python3
"function that appand a string to a text file"


def append_write(filename="", text=""):
    "function to appand"
    with open(filename, mode='a', encoding="utf-8") as f:
        p = f.write(text)
    return len(text)
