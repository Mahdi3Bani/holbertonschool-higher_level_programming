#!/usr/bin/python3


def uppercase(str):
    for i in str:
        if ord(i) > 96 and ord(i) < 123:
            c = chr(ord(i) - 32)
        else:
            c = i
            print("{}".format(c), end='')
    print()
