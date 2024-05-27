import unittest
from typing import List

"""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

    Each row must contain the digits 1-9 without repetition.
    Each column must contain the digits 1-9 without repetition.
    Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Note:

    A Sudoku board (partially filled) could be valid but is not necessarily solvable.
    Only the filled cells need to be validated according to the mentioned rules.

"""


def valid_sudoku(board: List[List[str]]) -> bool:
    row = [[0] * 9 for _ in board]
    column = [[0] * 9 for _ in board]
    box = [[0] * 9 for _ in board]
    for col_index, sudoku_row in enumerate(board):
        for index in range(0, 9):
            value = sudoku_row[index]
            if value == ".":
                continue

            target = int(sudoku_row[index]) - 1

            if row[index][target] != 0:
                return False
            else:
                row[index][target] = 1

            if column[col_index][target] != 0:
                return False
            else:
                column[col_index][target] = 1

            if box[(index // 3) * 3 + (col_index // 3)][target] != 0:
                return False
            else:
                box[(index // 3) * 3 + (col_index // 3)][target] = 1
    return True


# Space Complexity O(N^2)
# Time Complexity O(N^2)

class TestValid(unittest.TestCase):
    def setUp(self):
        self.example_valid_sudoku = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
                                     ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                                     [".", "9", "8", ".", ".", ".", ".", "6", "."],
                                     ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                                     ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                                     ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                                     [".", "6", ".", ".", ".", ".", "2", "8", "."],
                                     [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                                     [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
        self.example_invalid_sudoku = [["8", "3", ".", ".", "7", ".", ".", ".", "."],
                                       ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                                       [".", "9", "8", ".", ".", ".", ".", "6", "."],
                                       ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                                       ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                                       ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                                       [".", "6", ".", ".", ".", ".", "2", "8", "."],
                                       [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                                       [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

    def test_unique_pairs_k_diff(self):
        self.assertEqual(valid_sudoku(self.example_valid_sudoku), True)
        self.assertEqual(valid_sudoku(self.example_invalid_sudoku), False)
