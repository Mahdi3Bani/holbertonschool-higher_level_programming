#!/usr/bin/python3


from calendar import c


def uppercase(str):
    for i in str:
        print("{}".format(chr(ord(str) + 32)))
