#
# @lc app=leetcode id=3529 lang=python3
#
# [3529] Count Cells in Overlapping Horizontal and Vertical Substrings
#

from collections import Counter
# @lc code=start
class Solution:
    def countCells(self, grid: List[List[str]], pattern: str) -> int:
        top, bottom, left, right = 0, len(grid) - 1, 0, len(grid[0]) - 1
        vert_cells = set()
        hz_cells = set()

        # "abaca" -> {a: 3, b: 1, c: 1}
        # pattern_map = Counter(pattern)
        # perform vertical scan first





            
# @lc code=end