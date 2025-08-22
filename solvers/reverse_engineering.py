"""
Reverse Engineering Solver for Zip Puzzle
"""
import numpy as np
from utils.grid_utils import get_neighbors

class ReverseEngineeringSolver:
    def __init__(self, grid):
        self.grid = grid

    def solve(self):
        end = tuple(np.argwhere(self.grid == np.max(self.grid))[0])
        path = [end]
        for num in range(np.max(self.grid), 1, -1):
            prev = self._find_prev(path[-1], num - 1)
            if prev is None:
                return None
            path.append(prev)
        return path[::-1]

    def _find_prev(self, pos, num):
        for neighbor in get_neighbors(pos, self.grid.shape):
            if self.grid[neighbor] == num:
                return neighbor
        return None
