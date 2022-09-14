#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = []
    new1 = []
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            new1 = new1 + [matrix[i][j] ** 2]
        new = new + [new1]
        new1 = []
    return (new)
