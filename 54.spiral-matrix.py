#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#

# @lc code=start
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top, bottom, left, right = 0, len(matrix) - 1, 0, len(matrix[0]) - 1
        spiral = []
        while top <= bottom and left <= right:
            for i in range(left, right + 1):
                spiral.append(matrix[top][i])
            top += 1

            if top <= bottom:
                for j in range(top, bottom + 1):
                    spiral.append(matrix[j][right])
                right -= 1
            
            if top <= bottom and left <= right:
                for k in range(right, left - 1, -1):
                    spiral.append(matrix[bottom][k])
                bottom -= 1
            if top <= bottom and left <= right:
                for l in range(bottom, top - 1, -1):
                    spiral.append(matrix[l][left])
                left += 1
        return spiral
# @lc code=end

#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#

# @lc code=start