#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#

# @lc code=start
from typing import List
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        m, n = len(board[0]), len(board)
        # Check duplicates in each row
        for r in range(n):
            r_set = set()
            for c in range(m):
                if board[r][c] == ".":
                    continue
                if board[r][c] in r_set:
                    return False
                r_set.add(board[r][c])

        # Check duplicates in each column
        for c in range(m):
            c_set = set()
            for r in range(n):
                if board[r][c] == ".":
                    continue
                if board[r][c] in c_set:
                    return False
                c_set.add(board[r][c])

        # Check all the places in the box (3x3)
        box_starts = [(i, j) for i in range(0, 7, 3) for j in range(0, 7, 3)]
        for row, col in box_starts:
            box_set = set()
            for r in range(row, row+3):
                for c in range(col, col+3):
                    if board[r][c] == ".":
                        continue
                    if board[r][c] in box_set:
                        return False
                    box_set.add(board[r][c])
        return True
# @lc code=end

