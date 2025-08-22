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
        total_cells = self.grid.size
        path = [end]
        visited = set([end])
        if self._reverse_dfs(end, np.max(self.grid)-1, path, visited):
            if len(path) == total_cells and path[0] == end:
                return path[::-1]
        return None

    def _reverse_dfs(self, pos, next_num, path, visited):
        if len(path) == self.grid.size:
            nums_in_path = [self.grid[p] for p in path if self.grid[p] > 0]
            if nums_in_path[::-1] == list(range(1, np.max(self.grid)+1)):
                return True
            return False
        for neighbor in get_neighbors(pos, self.grid.shape):
            if neighbor not in visited:
                if self.grid[neighbor] > 0:
                    if self.grid[neighbor] != next_num:
                        continue
                    path.append(neighbor)
                    visited.add(neighbor)
                    if self._reverse_dfs(neighbor, next_num-1, path, visited):
                        return True
                    path.pop()
                    visited.remove(neighbor)
                else:
                    path.append(neighbor)
                    visited.add(neighbor)
                    if self._reverse_dfs(neighbor, next_num, path, visited):
                        return True
                    path.pop()
                    visited.remove(neighbor)
        return False
