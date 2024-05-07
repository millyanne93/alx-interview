#!/usr/bin/python3
"""
Minimum Operations
"""


def minOperations(n):
    '''Computes the fewest number of operations needed to result
    in exactly n H characters.

    Args:
        n (int): The target number of H characters.

    Returns:
        int: The fewest number of operations required.

    '''
    if not isinstance(n, int):
        return 0

    ops = 0
    clip = 0
    done = 1

    while done < n:
        if clip == 0:
            # Initialize (the first Copy All and Paste)
            clip = done
            done += clip
            ops += 2
        elif n - done > 0 and (n - done) % done == 0:
            # Copy All and Paste
            clip = done
            done += clip
            ops += 2
        elif clip > 0:
            # Paste
            done += clip
            ops += 1

    return ops
    
