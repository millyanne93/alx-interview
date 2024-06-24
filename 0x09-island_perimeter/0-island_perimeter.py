#!/usr/bin/python3
"""
A module that contains a function that returns the perimeter of an island
described in grid
"""


def island_perimeter(grid):
    """A function that outputs the perimeter of an island described by grid"""
    # Initialize the perimeter counter
    perimeter = 0

    # Get the number of rows and columns in the grid
    rows = len(grid)
    cols = len(grid[0])

    # Iterate over each cell in the grid
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                perimeter += 4

                if r > 0 and grid[r - 1][c] == 1:
                    perimeter -= 1

                if r < rows - 1 and grid[r + 1][c] == 1:
                    perimeter -= 1

                if c > 0 and grid[r][c - 1] == 1:
                    perimeter -= 1

                if c < cols - 1 and grid[r][c + 1] == 1:
                    perimeter -= 1

    return perimeter
