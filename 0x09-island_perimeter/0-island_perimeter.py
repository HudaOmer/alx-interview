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
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                cell = 4
                if (i > 0 and grid[i - 1][j] == 1):
                    cell -= 1
                if (i < n - 1 and grid[i + 1][j] == 1):
                    cell -= 1
                if (j > 0 and grid[i][j - 1] == 1):
                    cell -= 1
                if (j < m - 1 and grid[i][j + 1] == 1):
                    cell -= 1
                perimeter += cell
    return perimeter
