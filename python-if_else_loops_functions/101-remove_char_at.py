#!/usr/bin/python3

def remove_char_at(str, n):
    for i in len(str):
        if i != n:
            print("{}".format(str[i]), end='')
