#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#
[-4, -1, -1, 0, 1, 2]
from collections import defaultdict
from typing import List
# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = []
        for i in range(n - 2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j, k = i + 1, n - 1
            total =  nums[j] + nums[k] + nums[i]
            while j < k:
                if total == 0:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                elif total < 0:
                    j += 1
                else:
                    k -= 1 
        return res

sol = Solution()
print(sol.threeSum([-1,0,1,2,-1,-4]))
# @lc code=end

