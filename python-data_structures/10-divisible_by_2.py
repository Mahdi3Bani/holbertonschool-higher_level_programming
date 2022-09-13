#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new = []
    for i in my_list:
        if i % 2 == 0:
            new = new + [True]
        else:
            new = new + [False]
    return new
