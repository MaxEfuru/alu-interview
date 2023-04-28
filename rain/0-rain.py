#!/usr/bin/python3

"""
Rain function in python
"""


def rain(walls):
    """
    begins here
    """
  
    n = len(walls)
    if n == 0:
        return 0
    
    left_max = [0] * n
    right_max = [0] * n
    
    # Find the highest wall to the left of each wall
    left_max[0] = walls[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i-1], walls[i])
    
    # Find the highest wall to the right of each wall
    right_max[n-1] = walls[n-1]
    for i in range(n-2, -1, -1):
        right_max[i] = max(right_max[i+1], walls[i])
    
    # Calculate the amount of water retained by each wall
    water = 0
    for i in range(n):
        water += min(left_max[i], right_max[i]) - walls[i]
    
    return water if water >= 0 else 0
