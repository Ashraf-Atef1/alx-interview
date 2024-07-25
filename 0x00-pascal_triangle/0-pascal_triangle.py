#!/usr/bin/python3
"""
0-pascal_triangle
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the Pascal’s triangle of n
    """
    triangle = []
    if not isinstance(n, int) or n <= 0:
        return triangle
    for line in range(1, n + 1):
        row = []
        counter = 1
        for i in range(1, line + 1):
            row.append(counter)
            counter = round(counter * (line - i) / i)
        triangle.append(row)
    return triangle
