#!/usr/bin/python3
from unittest import result


def safe_print_division(a, b):
    try:
        r = a / b
    except ZeroDivisionError:
        r = None
    finally:
        print("Inside result: {}".format(r))
    return r
