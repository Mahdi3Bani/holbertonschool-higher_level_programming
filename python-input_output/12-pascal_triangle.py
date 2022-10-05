#!/usr/bin/python3
""""Technical interview preparation"""


def pascal_triangle(n):
    """"returns a list of lists of integers
    representing the Pascals triangle of n"""
    lisst = []
    if n <= 0:
        return lisst
    if n == 1:
        return [[1]]

    lisst = [[1]]
    for i in range(n-1):
        lisst.append([a+b for a, b in zip([0] + lisst[-1], lisst[-1] + [0])])
    return lisst
