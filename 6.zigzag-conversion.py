#
# @lc app=leetcode id=6 lang=python3
#
# [6] Zigzag Conversion
#

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
    
        zz_matrix = [[] for _ in range(numRows)]
        direction = 1  # 1 for down, -1 for up
        row = 0

        for char in s:
            zz_matrix[row].append(char)
            
            if direction == 1:
                row += 1
            else:
                row -= 1

            if row == 0:
                direction = 1
            elif row == numRows - 1:
                direction = -1

        return ''.join(''.join(rows) for rows in zz_matrix)

# @lc code=end

