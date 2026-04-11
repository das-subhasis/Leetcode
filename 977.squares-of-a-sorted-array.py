#
# @lc app=leetcode id=977 lang=python3
#
# [977] Squares of a Sorted Array
#

# @lc code=start
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left, right = 0, n - 1
        res = []
        while left <= right:
            if abs(nums[left] ** 2) < abs(nums[right] ** 2):
                res.append(nums[right]**2)
                right -= 1
            else:
                res.append(nums[left]**2)
                left += 1
        res.reverse()
        return res
# @lc code=end

