#!/usr/bin/python3


def uppercase(str):
    for i in str:
        if ord(c) > 96 and ord(c) < 123:
            print("{}".format(chr(ord(i) - 32)), end='')
        else:
            print("{}".format(i), end='')
