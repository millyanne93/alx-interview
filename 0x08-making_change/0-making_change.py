#!/usr/bin/python3
"""
Interview Question on: fewest number of coins needed to
meet a given amount total
"""
from collections import deque


def makeChange(coins, total):
    """ fewest number of coins needed to meet total """
    if total <= 0:
        return 0

    queue = deque([(0, 0)])  # (current_amount, num_coins)

    # Initialize a set to keep track of visited amounts
    visited = set()

    # Perform BFS
    while queue:
        current_amount, num_coins = queue.popleft()

        # If we reach the target amount, return the number of coins used
        if current_amount == total:
            return num_coins

        # Explore the next states by adding each coin to the current amount
        for coin in coins:
            new_amount = current_amount + coin

            # If the new amount is within the target
            # and hasn't been visited yet
            if new_amount <= total and new_amount not in visited:
                visited.add(new_amount)
                queue.append((new_amount, num_coins + 1))

    # If we exhaust the queue without finding the target amount, return -1
    return -1
