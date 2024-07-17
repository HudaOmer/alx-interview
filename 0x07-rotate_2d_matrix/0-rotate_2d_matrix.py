#!/usr/bin/python3
"""
0. Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):
    n = len(matrix)
    new_matrix = [[0 for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            new_matrix[i][j] = matrix[n-j-1][i]

    for i in range(n):
        for j in range(n):
            matrix[i][j] = new_matrix[i][j]
