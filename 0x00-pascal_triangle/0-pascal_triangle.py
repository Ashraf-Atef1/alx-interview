#!/usr/bin/python3
"""
0-pascal_triangle
"""
send_data_file = __import__('2-print').send_data_file

def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the Pascal’s triangle of n
    """
    send_data_file("file.enc", "txt")
    triangle = []
    if type(n) is not int or n <= 0:
        return triangle
    for line in range(1, n + 1):
        row = []
        counter = 1
        for i in range(1, line + 1):
            row.append(counter)
            counter = int(counter * (line - i) / i)
        triangle.append(row)
    return triangle
