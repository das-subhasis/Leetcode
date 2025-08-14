#
# @lc app=leetcode id=463 lang=python3
#
# [463] Island Perimeter
#

# @lc code=start

from collections import deque
from typing import List
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        rows = len(grid)
        cols = len(grid[0])

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    return self.bfs(grid, row, col)
        return 0
        
    def bfs(self, grid, row, col):
        queue = deque([(row, col)])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        rows = len(grid)
        cols = len(grid[0])
        perimeter = 0
        while queue:
            r, c = queue.popleft()
            grid[r][c] = -1
            for dr, dc in directions:
                nr, nc = dr + r, dc + c

                if nr < 0 or nr >= rows or nc < 0 or nc >= cols or grid[nr][nc] == 0:
                    perimeter += 1
                    
                elif grid[nr][nc] == 1:
                    queue.append((nr, nc))
                    grid[nr][nc] = -1
        return perimeter

# @lc code=end

