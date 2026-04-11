#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#

# @lc code=start
from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # nums.sort() # technically since we are sorting it is not O(n)
        # max_len = 1
        # seq = 1
        # if not nums: return 0
        # for i in range(len(nums) - 1):
        #     if nums[i] == nums[i + 1]:
        #         continue
        #     if nums[i] + 1 == nums[i + 1]:
        #         seq += 1
        #     else:
        #         seq = 1
        #     max_len = max(seq, max_len)
        # return max_len

        s = set(nums)
        max_len = 0
        for num in s:
            if num - 1 not in s:
                next_num = num + 1
                length = 1
                while next_num in s:
                    next_num += 1
                    length += 1
                max_len = max(max_len, length)
        return max_len
                
# @lc code=end

