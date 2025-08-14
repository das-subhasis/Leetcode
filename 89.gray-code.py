#
# @lc app=leetcode id=89 lang=python3
#
# [89] Gray Code
#

# @lc code=start
class Solution:
    def grayCode(self, n: int) -> list[int]:
        return [ i ^ (i >> 1) for i in range(1 << n)]
# @lc code=end

