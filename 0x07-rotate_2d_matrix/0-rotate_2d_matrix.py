#!/usr/bin/python3
"""
Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """
    Rotate a 2D matrix 90 degrees clockwise.
    """
    n = len(matrix)
    for i in range(n // 2):  # Iterate over each layer
        # Iterate over each element in the current layer
        for j in range(i, n - i - 1):
            # Save the value of the top element
            tmp = matrix[i][j]

            # Move left element to top
            matrix[i][j] = matrix[n - 1 - j][i]

            # Move bottom element to left
            matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1 - j]

            # Move right element to bottom
            matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i]

            # Move top element to right
            matrix[j][n - 1 - i] = tmp
