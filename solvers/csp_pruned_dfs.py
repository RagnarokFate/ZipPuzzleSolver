"""
CSP Pruned DFS/A* Solver for Zip Puzzle
"""
import numpy as np
from utils.grid_utils import get_neighbors

class CSPPrunedDFSSolver:
    def __init__(self, grid):
        self.grid = grid

    def solve(self):
        start = tuple(np.argwhere(self.grid == 1)[0])
        end = tuple(np.argwhere(self.grid == np.max(self.grid))[0])
        total_cells = np.sum(self.grid != -1)
        path = [start]
        visited = set([start])
        result = self._dfs(start, 2, path, visited)
        if result and len(result) == total_cells and result[-1] == end:
            return result
        return None

    def _dfs(self, pos, next_num, path, visited):
        if len(path) == np.sum(self.grid != -1):
            nums_in_path = [self.grid[p] for p in path if self.grid[p] > 0]
            if nums_in_path == list(range(1, np.max(self.grid)+1)):
                return path.copy()
            return None
        # Pruning: if no possible moves, return None
        moves = [n for n in get_neighbors(pos, self.grid.shape)
                 if n not in visited and self.grid[n] != -1]
        if not moves:
            return None
        # Heuristic: prefer neighbors closer to next numbered cell
        targets = np.argwhere(self.grid == next_num)
        for neighbor in sorted(moves, key=lambda n: min([abs(n[0]-t[0])+abs(n[1]-t[1]) for t in targets]) if len(targets) else 0):
            if self.grid[neighbor] > 0:
                if self.grid[neighbor] != next_num:
                    continue
                path.append(neighbor)
                visited.add(neighbor)
                result = self._dfs(neighbor, next_num+1, path, visited)
                if result:
                    return result
                path.pop()
                visited.remove(neighbor)
            else:
                path.append(neighbor)
                visited.add(neighbor)
                result = self._dfs(neighbor, next_num, path, visited)
                if result:
                    return result
                path.pop()
                visited.remove(neighbor)
        return None
