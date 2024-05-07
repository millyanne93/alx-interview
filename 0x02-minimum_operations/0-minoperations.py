#!/usr/bin/python3
"""
Minimum Operations
"""


def minOperations(n):
    '''Computes the fewest number of operations needed to result
    in exactly n H characters using prime factorization.

    Args:
        n (int): The target number of H characters.

    Returns:
        int: The fewest number of operations required.

    '''
    if not isinstance(n, int) or n <= 0:
        return 0

    # Perform prime factorization of n
    operations = 0
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations
