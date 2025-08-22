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
        end = tuple(np.argwhere(self.grid == np.max(self.grid))[0])
        total_cells = self.grid.size
        self._dfs(start, [start], 2)
        # Only return if all cells are visited and ends at last number
        if self.found and len(self.path) == total_cells and self.path[-1] == end:
            return self.path
        return None

    def _dfs(self, pos, path, next_num):
        if len(path) == self.grid.size:
            # Check if all numbered cells are visited in order
            nums_in_path = [self.grid[p] for p in path if self.grid[p] > 0]
            if nums_in_path == list(range(1, np.max(self.grid)+1)):
                self.found = True
                self.path = path.copy()
            return
        for neighbor in get_neighbors(pos, self.grid.shape):
            if neighbor not in path:
                # If next cell is numbered, must match next_num
                if self.grid[neighbor] > 0:
                    if self.grid[neighbor] != next_num:
                        continue
                    self._dfs(neighbor, path + [neighbor], next_num + 1)
                else:
                    self._dfs(neighbor, path + [neighbor], next_num)
                if self.found:
                    return
