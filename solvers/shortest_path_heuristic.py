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
        path = []
        for num in range(1, np.max(self.grid)):
            start = tuple(np.argwhere(self.grid == num)[0])
            end = tuple(np.argwhere(self.grid == num + 1)[0])
            segment = self._bfs(start, end)
            if not segment:
                return None
            path += segment[:-1]
        path.append(tuple(np.argwhere(self.grid == np.max(self.grid))[0]))
        return path

    def _bfs(self, start, end):
        queue = deque([(start, [start])])
        visited = set([start])
        while queue:
            pos, path = queue.popleft()
            if pos == end:
                return path
            for neighbor in get_neighbors(pos, self.grid.shape):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, path + [neighbor]))
        return None
