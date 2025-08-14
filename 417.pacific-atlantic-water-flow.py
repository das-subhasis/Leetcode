#
# @lc app=leetcode id=417 lang=python3
#
# [417] Pacific Atlantic Water Flow
#

# @lc code=start
from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rowLen = len(heights)
        colLen = len(heights[0])
        atlantic = set()
        pacific = set()

        def dfs(row, col, visited, prevHeight):
            if row < 0 or row == rowLen or col < 0 or col == colLen:
                return
            
            if heights[row][col] < prevHeight:
                return
            
            if (row, col) in visited:
                return
            
            visited.add((row, col))
            
            dfs(row + 1, col, visited, heights[row][col])
            dfs(row - 1, col, visited, heights[row][col])
            dfs(row, col + 1, visited, heights[row][col])
            dfs(row, col - 1, visited, heights[row][col])

        for c in range(colLen):
            dfs(0, c, pacific, heights[0][c])
            dfs(rowLen - 1, c, atlantic, heights[rowLen - 1][c])
        
        for r in range(rowLen):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, colLen - 1, atlantic, heights[r][colLen - 1])

        return [(row, col) for row, col in atlantic.intersection(pacific)]
        
        
# @lc code=end

