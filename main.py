"""
Main entry point for Zip Puzzle Solver
"""
import numpy as np
from puzzles.sample_puzzles import get_all_puzzles
from solvers.brute_force import BruteForceSolver
from solvers.divide_conquer_dp import DivideConquerDPSolver
from solvers.shortest_path_heuristic import ShortestPathHeuristicSolver
from solvers.reverse_engineering import ReverseEngineeringSolver
from solvers.ml_predictor import MLPredictorSolver
from visualization.animator import ZipPuzzleAnimator
from visualization.panel_layout import get_panel_titles


def main():
    puzzles = get_all_puzzles()
    for name, grid in puzzles:
        print(f"\n--- {name} ---")
        solvers = [
            BruteForceSolver(grid),
            DivideConquerDPSolver(grid),
            ShortestPathHeuristicSolver(grid),
            ReverseEngineeringSolver(grid),
            MLPredictorSolver(grid)
        ]
        paths = [solver.solve() or [] for solver in solvers]
        titles = get_panel_titles()
        print("Solutions:")
        for t, p in zip(titles, paths):
            print(f"{t}: {'Found' if p else 'No Solution'}")
        animator = ZipPuzzleAnimator(grid, paths, titles)
        animator.animate()

if __name__ == "__main__":
    main()
