#!/usr/bin/python3
"""method that determines if all the boxes can be opened"""

from collections import deque


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.

    Args:
    - boxes (list of lists): List of lists representing the boxes
    and keys they contain.

    Returns:
    - bool: True if all boxes can be opened, False otherwise.
    """
    if not boxes:
        return False

    n = len(boxes)
    visited = set()
    queue = deque([0])  # Start with the first box

    while queue:
        box_index = queue.popleft()
        visited.add(box_index)
        keys = boxes[box_index]

        for key in keys:
            if 0 <= key < n and key not in visited:
                queue.append(key)

    return len(visited) == n
