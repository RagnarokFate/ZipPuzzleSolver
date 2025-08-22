"""
Shortest Path + Heuristic Solver for Zip Puzzle
"""
import numpy as np
from utils.grid_utils import get_neighbors
from collections import deque


class ShortestPathHeuristicSolver:
    def __init__(self, grid):
        self.grid = grid

    def solve(self):
        start = tuple(np.argwhere(self.grid == 1)[0])
        end = tuple(np.argwhere(self.grid == np.max(self.grid))[0])
        total_cells = self.grid.size
        path = [start]
        visited = set([start])
        result = self._backtrack(start, 2, path, visited)
        if result and len(result) == total_cells and result[-1] == end:
            return result
        return None

    def _backtrack(self, pos, next_num, path, visited):
        if len(path) == self.grid.size:
            nums_in_path = [self.grid[p] for p in path if self.grid[p] > 0]
            if nums_in_path == list(range(1, np.max(self.grid)+1)):
                return path.copy()
            return None
        for neighbor in get_neighbors(pos, self.grid.shape):
            if neighbor not in visited:
                if self.grid[neighbor] > 0:
                    if self.grid[neighbor] != next_num:
                        continue
                    path.append(neighbor)
                    visited.add(neighbor)
                    result = self._backtrack(neighbor, next_num + 1, path, visited)
                    if result:
                        return result
                    path.pop()
                    visited.remove(neighbor)
                else:
                    path.append(neighbor)
                    visited.add(neighbor)
                    result = self._backtrack(neighbor, next_num, path, visited)
                    if result:
                        return result
                    path.pop()
                    visited.remove(neighbor)
        return None
