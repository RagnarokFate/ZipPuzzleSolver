"""
ML Predictor Solver for Zip Puzzle (stub)
"""
import numpy as np


class MLPredictorSolver:
    def __init__(self, grid):
        self.grid = grid

    def solve(self):
        # Simple heuristic: always move to neighbor closest to next target
        path = []
        current = tuple(np.argwhere(self.grid == 1)[0])
        path.append(current)
        for num in range(2, np.max(self.grid)+1):
            target = tuple(np.argwhere(self.grid == num)[0])
            neighbors = [n for n in self._get_neighbors(current) if n not in path]
            if not neighbors:
                return None
            # Pick neighbor with minimum Manhattan distance to target
            next_step = min(neighbors, key=lambda n: abs(n[0]-target[0]) + abs(n[1]-target[1]))
            path.append(next_step)
            current = next_step
        return path

    def _get_neighbors(self, pos):
        x, y = pos
        neighbors = []
        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.grid.shape[0] and 0 <= ny < self.grid.shape[1]:
                neighbors.append((nx, ny))
        return neighbors
