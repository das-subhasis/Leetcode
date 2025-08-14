#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        goal = n - 1
        for i in range(n - 2, -1, -1):
            if nums[i] + i >= goal:
                goal = i
        if goal == 0:
            return True
        return False
# @lc code=end

