"""
Brute Force Solver for Zip Puzzle
"""
import numpy as np
from utils.grid_utils import get_neighbors

class BruteForceSolver:
    def __init__(self, grid):
        self.grid = grid
        self.numbers = np.sort(grid.flatten())
        self.path = []
        self.found = False

    def solve(self):
        start = tuple(np.argwhere(self.grid == 1)[0])
        self._dfs(start, [start], 2)
        return self.path if self.found else None

    def _dfs(self, pos, path, next_num):
        if next_num > self.numbers[-1]:
            self.found = True
            self.path = path.copy()
            return
        for neighbor in get_neighbors(pos, self.grid.shape):
            if self.grid[neighbor] == next_num and neighbor not in path:
                self._dfs(neighbor, path + [neighbor], next_num + 1)
                if self.found:
                    return
