"""
Animator for Zip Puzzle Solver
"""
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

class ZipPuzzleAnimator:
    def __init__(self, grid, solver_paths, titles):
        self.grid = grid
        self.solver_paths = solver_paths
        self.titles = titles

    def animate(self):
        fig, axes = plt.subplots(1, len(self.solver_paths), figsize=(5 * len(self.solver_paths), 5))
        if len(self.solver_paths) == 1:
            axes = [axes]
        max_len = max(len(path) for path in self.solver_paths)
        grid_shape = self.grid.shape
        for step in range(max_len):
            for i, (ax, path, title) in enumerate(zip(axes, self.solver_paths, self.titles)):
                ax.clear()
                ax.set_title(title)
                # Draw grid
                ax.set_xticks(np.arange(-0.5, grid_shape[1], 1), minor=True)
                ax.set_yticks(np.arange(-0.5, grid_shape[0], 1), minor=True)
                ax.grid(which='minor', color='black', linestyle='-', linewidth=1)
                ax.imshow(np.ones(grid_shape), cmap='Greys', vmin=0, vmax=1, alpha=0.2)
                # Draw cell numbers
                for x in range(grid_shape[0]):
                    for y in range(grid_shape[1]):
                        val = self.grid[x, y]
                        if val > 0:
                            ax.text(y, x, str(val), color='black', ha='center', va='center', fontsize=14, fontweight='bold')
                # Animate path
                if not path:
                    ax.text(grid_shape[1]/2, grid_shape[0]/2, 'No Solution', color='red', fontsize=16, ha='center', va='center')
                else:
                    # Draw lines between steps
                    for j in range(1, min(step+1, len(path))):
                        prev = path[j-1]
                        curr = path[j]
                        if step == len(path)-1:
                            color = 'green'
                        elif step+1 == max_len and step != len(path)-1:
                            color = 'red'
                        else:
                            color = 'blue'
                        ax.plot([prev[1], curr[1]], [prev[0], curr[0]], color=color, linewidth=3, alpha=0.7)
                    # Draw current position
                    if step < len(path):
                        curr = path[step]
                        ax.plot(curr[1], curr[0], 'o', color='orange', markersize=14)
                ax.set_xlim(-0.5, grid_shape[1]-0.5)
                ax.set_ylim(grid_shape[0]-0.5, -0.5)
                ax.set_xticks([])
                ax.set_yticks([])
        plt.tight_layout()
        plt.show()
