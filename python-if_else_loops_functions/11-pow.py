#!/usr/bin/python3


def pow(a, b):
    p = 1
    if b < 0:
        l = b * -1
    for i in range(1, l + 1):
        p = p * a
    if b < 0:
        return 1 / p
    return (p)
