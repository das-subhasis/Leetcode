#
# @lc app=leetcode id=2226 lang=python3
#
# [2226] Maximum Candies Allocated to K Children
#

# @lc code=start
import heapq
from typing import List
class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        l, r = 1, max(candies)

        while l <= r:
            mid = (l + r) // 2
            total_candies = sum(pile // mid for pile in candies)

            if total_candies >= k:
                l = mid + 1
            else:
                r = mid - 1
        return r
# @lc code=end

