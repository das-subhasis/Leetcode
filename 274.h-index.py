#
# @lc app=leetcode id=274 lang=python3
#
# [274] H-Index
#

# @lc code=start
from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        hIndex = 0

        for i in range(len(citations)):
            if i < citations[i]:
                hIndex += 1
        
        return hIndex
        
# @lc code=end

