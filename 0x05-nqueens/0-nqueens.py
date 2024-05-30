#!/usr/bin/python3
""" N Queens Problem """
import sys


def validate_input():
    """ Validates the input arguments """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)

    if not sys.argv[1].isdigit():
        print("N must be a number")
        exit(1)

    n = int(sys.argv[1])

    if n < 4:
        print("N must be at least 4")
        exit(1)

    return n


def generate_solutions(n, row=0, columns=None,
                       major_diagonals=None, minor_diagonals=None):
    """ Generates solutions to the N Queens problem """
    if columns is None:
        columns = []
    if major_diagonals is None:
        major_diagonals = []
    if minor_diagonals is None:
        minor_diagonals = []

    if row < n:
        for col in range(n):
            if (col not in columns and
                    row + col not in major_diagonals and
                    row - col not in minor_diagonals):
                yield from generate_solutions(
                    n, row + 1,
                    columns + [col],
                    major_diagonals + [row + col],
                    minor_diagonals + [row - col]
                )
    else:
        yield columns


def solve_nqueens(n):
    """ Solves the N Queens problem and prints each solution """
    for solution in generate_solutions(n):
        print([[row, col] for row, col in enumerate(solution)])


if __name__ == "__main__":
    n = validate_input()
    solve_nqueens(n)
