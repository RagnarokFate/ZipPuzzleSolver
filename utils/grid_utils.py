"""
Grid utility functions for Zip Puzzle
"""
import numpy as np

def get_neighbors(pos, shape):
    """Return valid neighboring positions (up, down, left, right) for a cell."""
    x, y = pos
    neighbors = []
    for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < shape[0] and 0 <= ny < shape[1]:
            neighbors.append((nx, ny))
    return neighbors
