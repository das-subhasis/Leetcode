#
# @lc app=leetcode id=96 lang=python3
#
# [96] Unique Binary Search Trees
#

# @lc code=start
class Solution:
    def numTrees(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
        dp = [1] * (n+1)
        for node in range(2, n + 1):
            total = 0
            for root in range(1, node + 1):
                total += dp[root - 1] * dp[node - root]
            dp[node] = total
        return dp[n]
# @lc code=end

