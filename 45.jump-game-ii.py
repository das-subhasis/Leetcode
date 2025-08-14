#
# @lc app=leetcode id=45 lang=python3
#
# [45] Jump Game II
#

# @lc code=start
from typing import List
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        min_jumps = 0
        goal = 0
        max_reach = 0
        if len(nums) == 1:
            return 0
        for i in range(n - 1):
            max_reach = max(max_reach, nums[i] + i)
            
            if i == goal:
                min_jumps += 1
                goal = max_reach
        return min_jumps
sol = Solution()
print(sol.jump([2,3,1,1,4]
))
        
# @lc code=end

