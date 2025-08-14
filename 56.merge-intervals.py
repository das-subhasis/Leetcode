#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#

# @lc code=start
from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key = lambda x : x[0])
        n = len(intervals)
        res = [intervals[0]]

        for i in range(1, n):
            
            curr = intervals[i]
            prev = res[-1]

            if prev[1] >= curr[0]:
                prev[1] = max(curr[1], prev[1])
            else:
                res.append(curr)
        return res
        
sol = Solution()
print(sol.merge([[1,3],[2,6],[8,10],[15,18]]))
# @lc code=end

