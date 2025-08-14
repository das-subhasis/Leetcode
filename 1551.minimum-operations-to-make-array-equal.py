#
# @lc app=leetcode id=1551 lang=python3
#
# [1551] Minimum Operations to Make Array Equal
#

# @lc code=start
class Solution:
    def minOperations(self, n: int) -> int:
        if n % 2 == 0:
            return (n // 2) ** 2
        else:
            return (n // 2) * (n // 2 + 1)
    
# @lc code=end

