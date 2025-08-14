#
# @lc app=leetcode id=670 lang=python3
#
# [670] Maximum Swap
#

# @lc code=start
import heapq
class Solution:
    def maximumSwap(self, num: int) -> int:
        # nums_list = list(str(num))
        # nums = [str(num)]
        # if num < 100:
        #     return int(max(str(num), str(num)[::-1]))
        # for i in range(len(nums_list) - 1):
        #     for j in range(i + 1, len(nums_list)):
        #         nums_list[i], nums_list[j] = nums_list[j], nums_list[i]
        #         nums.append(''.join(nums_list))
        #         nums_list[i], nums_list[j] = nums_list[j], nums_list[i]
        # nums = [int(n) for n in nums]
        # return max(nums) if nums else num
        nums_list = [-1] * len(str(num))
        stack = []
        for i in range(len(str(num) - 1, -1, -1)):
            if stack and stack[-1]

# @lc code=end

