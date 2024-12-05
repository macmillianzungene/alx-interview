# Island Perimeter Function

This repository contains a Python function `island_perimeter(grid)` that calculates the perimeter of an island represented in a grid.

## Function Overview

The `island_perimeter` function takes a grid of integers as input and returns the perimeter of the island described in the grid. The grid is a list of lists, where:
- `0` represents water
- `1` represents land

Each cell in the grid is square with a side length of 1, and cells are connected horizontally or vertically. The grid is completely surrounded by water, ensuring that there is only one island (or none).

## Input Format

The input to the function is a rectangular grid (list of lists) with the following characteristics:
- The grid width and height do not exceed 100.
- The grid is completely surrounded by water.
- There is only one island in the grid, and the island does not contain any lakes (water inside that isn’t connected to the water surrounding the island).

### Example Grid


