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
        total_cells = self.grid.size
        bitmask = 1 << (start[0] * self.grid.shape[1] + start[1])
        path = self._dp(start, 2, bitmask, [start])
        if path and len(path) == total_cells:
            return path
        return None

    def _dp(self, pos, next_num, bitmask, path):
        key = (pos, next_num, bitmask)
        if key in self.memo:
            return self.memo[key]
        if len(path) == self.grid.size:
            nums_in_path = [self.grid[p] for p in path if self.grid[p] > 0]
            if nums_in_path == list(range(1, np.max(self.grid)+1)):
                return path.copy()
            return None
        for neighbor in get_neighbors(pos, self.grid.shape):
            idx = neighbor[0] * self.grid.shape[1] + neighbor[1]
            if not (bitmask & (1 << idx)):
                if self.grid[neighbor] > 0:
                    if self.grid[neighbor] != next_num:
                        continue
                    result = self._dp(neighbor, next_num + 1, bitmask | (1 << idx), path + [neighbor])
                else:
                    result = self._dp(neighbor, next_num, bitmask | (1 << idx), path + [neighbor])
                if result:
                    self.memo[key] = [pos] + result[1:]
                    return self.memo[key]
        self.memo[key] = None
        return None
