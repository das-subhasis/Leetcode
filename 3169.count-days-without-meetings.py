#
# @lc app=leetcode id=3169 lang=python3
#
# [3169] Count Days Without Meetings
#

# @lc code=start
from typing import List
class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort(key = lambda x: x[0])
        n = len(meetings)
        res = [meetings[0]]
        count = 0
        for i in range(1, n):
            curr = meetings[i]
            prev = res[-1]

            if curr[0] <= prev[1]:
                prev[1] = max(prev[1], curr[1])
            else:
                res.append(curr)
        for start, end in res:
            count += (end - start + 1)
        return days - count
        
sol = Solution()
print(sol.countDays(10, [[5,7],[1,3],[9,10]]))

# @lc code=end

