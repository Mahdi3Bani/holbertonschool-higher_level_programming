#!/usr/bin/python3


def uppercase(str):
    for i in str:
        print("{}".format(chr(ord(str[i]) + 32)), end='')
