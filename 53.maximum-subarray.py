#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSum, total = 0, float('-inf')
        n = len(nums)
        for i in range(n):
            if currSum <= 0:
                currSum = nums[i]
            else:
                currSum += nums[i]
            total = max(currSum, total)
        return total
# @lc code=end

