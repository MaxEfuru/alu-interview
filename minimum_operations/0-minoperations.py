#!/usr/bin/python3

def minOperations(n):
    if n == 1:
        return 0  # only one H, no operations needed
    if n < 1:
        return 0  # invalid input, impossible to achieve
    for i in range(2, n+1):
        if n % i == 0:
            return minOperations(n//i) + i  # recursively compute minimum number of operations
    return 0  # n is prime or 1, impossible to achieve
