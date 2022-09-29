#!/usr/bin/python3
class MyList(list):
    """"subclass"""

    def print_sorted(self):
        a = sorted(self)
        print (a)