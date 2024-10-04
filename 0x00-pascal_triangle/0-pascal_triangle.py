#!/usr/bin/env python3
"""
Generate Pascal's Triangle up to the nth row.

This function generates Pascal's Triangle up to the specified number of rows.
Pascal's Triangle is a triangular array of the binomial coefficients.

Args:
    n (int): The number of rows of Pascal's Triangle to generate.

Returns:
    list: A list of lists, where each inner list represents a row of Pascal's Triangle.
"""

def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = [[1]]
    
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)
    
    return triangle

