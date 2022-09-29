#!/usr/bin/python3
"""Inheretence from builtin."""


class MyList(list):
    """"subclass"""

    def print_sorted(self):
        a = sorted(self)
        print(a)
