#
# @lc app=leetcode id=3396 lang=python3
#
# [3396] Minimum Number of Operations to Make Elements in Array Distinct
#

# @lc code=start
class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        minOps = 0
        def isDistinct(arr): return len(arr) == len(set(arr))
        if isDistinct(nums):
            print(isDistinct(nums))
            return minOps
        while len(nums) >= 3 and not isDistinct(nums):
            nums = nums[3:]
            minOps += 1
        if nums and not isDistinct(nums):
            minOps += 1
        return minOps

sol = Solution()
print(sol.minimumOperations([4,5,6,4,4]))        
# @lc code=end

