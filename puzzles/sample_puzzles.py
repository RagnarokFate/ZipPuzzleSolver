"""
Sample puzzles for Zip Puzzle Solver
"""
import numpy as np

# Valid 3x3 puzzle (snake path)
def get_puzzle_3x3():
    return np.array([
        [1, 2, 3],
        [6, 5, 4],
        [7, 8, 9]
    ])

# Valid 4x4 puzzle (spiral)
def get_puzzle_4x4():
    return np.array([
        [ 1,  2,  3,  4],
        [12, 13, 14,  5],
        [11, 16, 15,  6],
        [10,  9,  8,  7]
    ])

# Valid 5x5 puzzle (zigzag)
def get_puzzle_5x5():
    return np.array([
        [ 1,  2,  3,  4,  5],
        [10,  9,  8,  7,  6],
        [11, 12, 13, 14, 15],
        [20, 19, 18, 17, 16],
        [21, 22, 23, 24, 25]
    ])

# Invalid puzzle (for negative test)
def get_invalid_puzzle():
    return np.array([
        [1, 0, 0],
        [0, 2, 0],
        [0, 0, 3]
    ])

# Today's puzzle (6x6, ignore barriers)
def get_puzzle_today():
    # 0 = blank, 1-6 = numbered cells
    arr = np.zeros((6,6), dtype=int)
    arr[0,0] = 1
    arr[0,5] = 6
    arr[2,2] = 4
    arr[2,4] = 2
    arr[4,1] = 3
    arr[4,3] = 5
    return arr

# Return all puzzles for batch testing
def get_all_puzzles():
    return [
        ("3x3 Snake", get_puzzle_3x3()),
        ("4x4 Spiral", get_puzzle_4x4()),
        ("5x5 Zigzag", get_puzzle_5x5()),
        ("Today's Puzzle", get_puzzle_today()),
        ("Invalid", get_invalid_puzzle()),
    ]
