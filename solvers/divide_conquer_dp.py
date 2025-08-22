"""
Divide & Conquer + DP Solver for Zip Puzzle
"""
import numpy as np
from utils.grid_utils import get_neighbors


class DivideConquerDPSolver:
    def __init__(self, grid):
        self.grid = grid
        self.n = grid.shape[0] * grid.shape[1]
        self.memo = {}

    def solve(self):
        start = tuple(np.argwhere(self.grid == 1)[0])
        bitmask = 1 << (start[0] * self.grid.shape[1] + start[1])
        path = self._dp(start, 2, bitmask)
        if path:
            return path
        return None

    def _dp(self, pos, next_num, bitmask):
        key = (pos, next_num, bitmask)
        if key in self.memo:
            return self.memo[key]
        if next_num > np.max(self.grid):
            return [pos]
        for neighbor in get_neighbors(pos, self.grid.shape):
            idx = neighbor[0] * self.grid.shape[1] + neighbor[1]
            if self.grid[neighbor] == next_num and not (bitmask & (1 << idx)):
                result = self._dp(neighbor, next_num + 1, bitmask | (1 << idx))
                if result:
                    self.memo[key] = [pos] + result
                    return self.memo[key]
        self.memo[key] = None
        return None
