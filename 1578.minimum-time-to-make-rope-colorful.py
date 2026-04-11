#
# @lc app=leetcode id=1578 lang=python3
#
# [1578] Minimum Time to Make Rope Colorful
#

# @lc code=start
from typing import List
class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        start, minTime = 0, 0

        for i in range(1, len(colors)):
            if colors[start] == colors[i]:
                minTime += min(neededTime[start], neededTime[i])
                if neededTime[i] > neededTime[start]:
                    start = i
            else:
                start = i
        return minTime

# @lc code=end

