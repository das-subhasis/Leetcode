#
# @lc app=leetcode id=48 lang=python3
#
# [48] Rotate Image
#

# @lc code=start
from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n, m = len(matrix), len(matrix[0])
        c_mid = m // 2

        for i in range(n):
            for j in range(i + 1, m):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        for k in range(n):
            for l in range(c_mid):
                matrix[k][l], matrix[k][m - 1 - l] = matrix[k][m - 1 - l], matrix[k][l]

# sol = Solution()
# matrix = [[1,2,3],[4,5,6],[7,8,9]]
# sol.rotate(matrix)
# print(matrix)
        

# @lc code=end

