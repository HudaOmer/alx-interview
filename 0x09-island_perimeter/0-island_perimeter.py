#!/usr/bin/python3
"""
0. Island Perimeter
"""


def island_perimeter(grid):
    """
    Returns the perimeter of the island described in grid
    """
    n = len(grid)
    m = len(grid[0])
    perimeter = 0
    for i in range(1, n - 1):
        for j in range(1, m - 1):
            if grid[i][j] == 0:
                pass
            else:
                if grid[i - 1][j] == 0:
                    perimeter += 1
                if grid[i + 1][j] == 0:
                    perimeter += 1
                if grid[i][j - 1] == 0:
                    perimeter += 1
                if grid[i][j + 1] == 0:
                    perimeter += 1
    return perimeter
