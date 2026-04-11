#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index = dict()
        for i, num in enumerate(nums):
            if num not in index:
                index[target - num] = i
            else:
                return [index[num], i] 
        return []

solution = Solution()
solution.twoSum([1, 2, 3], 2)
# @lc code=end

