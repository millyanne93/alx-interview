#!/usr/bin/python3
"""
Greedy Algorithm for Coin Change Problem
"""


def makeChange(coins, total):
    """Calculate the fewest number of coins needed
    to meet a given total amount.
    """
    if total <= 0:
        return 0

    # Sort coins in descending order
    coins.sort(reverse=True)

    num_coins = 0
    for coin in coins:
        if total == 0:
            break
        if coin <= total:
            num_coins += total // coin
            total %= coin

    return -1 if total > 0 else num_coins
