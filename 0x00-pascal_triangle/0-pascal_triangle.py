#!/usr/bin/python3
"""
Generate Pascal's Triangle up to the nth row
"""


def pascal_triangle(n):
    """This function generates Pascal's Triangle up to the specified number of rows.
Pascal's Triangle is a triangular array of the binomial coefficients.

Args:
    n (int): The number of rows of Pascal's Triangle to generate.

Returns:
    list: A list of lists, where each inner list represents a row of Pascal's Triangle.
    """
    triangle = []
    if n > 0:
        for i in range(1, n + 1):
            row = []
            b = 1
            for j in range(1, i + 1):
                row.append(b)
                b = b * (i - j) // j
            triangle.append(row)
    return triangle
