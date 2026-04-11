#
# @lc app=leetcode id=228 lang=python3
#
# [228] Summary Ranges
#

# @lc code=start
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ranges = []
        if not nums:
            return ranges
        
        if len(nums) == 1:
            return [f"{nums[0]}"]
        
        lo, hi = 0, 0

        i = 0

        while i < len(nums) - 1:
            if nums[i] + 1 == nums[i + 1]:
                hi = i + 1
            else:
                if lo == hi:
                    ranges.append(f"{nums[lo]}")
                else:
                    ranges.append(f"{nums[lo]}->{nums[hi]}")
                hi = lo = i + 1
            i += 1
        if i < len(nums):
            if lo == hi:
                ranges.append(f"{nums[lo]}")
            else:
                ranges.append(f"{nums[lo]}->{nums[hi]}")



        return ranges
# @lc code=end

