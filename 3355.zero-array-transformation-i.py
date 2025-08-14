#
# @lc app=leetcode id=3355 lang=python3
#
# [3355] Zero Array Transformation I
#

# @lc code=start
class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        delta = [0] * (n + 1)  

        for li, ri in queries:
            delta[li] += 1
            if ri + 1 < n:
                delta[ri + 1] -= 1

        coverage = [0] * n
        coverage[0] = delta[0]
        for i in range(1, n):
            coverage[i] = coverage[i - 1] + delta[i]

        for i in range(n):
            if coverage[i] < nums[i]:  
                return False

        return True
# @lc code=end

