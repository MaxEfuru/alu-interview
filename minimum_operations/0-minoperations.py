#!/usr/bin/python3
# define function

"""
Goo
"""

def minOperations(n):
    """
    Calculates the fewest number of operations needed to result in exactly n H characters in a text file.

    Args:
        n (int): the desired number of H characters

    Returns:
        int: the minimum number of operations needed to achieve n H's in the file

    Raises:
        None

    Example:
        >>> minOperations(6)
        5
    """
    if n == 1:
        return 0  # only one H, no operations needed
    if n < 1:
        return 0  # invalid input, impossible to achieve
    for i in range(2, n+1):
        if n % i == 0:
            return minOperations(n//i) + i  # recursively compute minimum number of operations
    return 0  # n is prime or 1, impossible to achieve
