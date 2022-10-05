#!/usr/bin/python3
""""Technical interview preparation"""


def pascal_triangle(n):
    """"returns a list of lists of integers representing the Pascal’s triangle of n"""
    lisst = []
    if n <= 0:
        return lisst
    else:
        for i in range(n):
            lisst += []
            for j in range(i + 1):
                if i > 1 and j < 1 and j != 0:
                    lisst += lisst[i-1][j] + lisst[i-1][j-1]
                elif j != n:
                    lisst[i] += [1]
    return lisst
