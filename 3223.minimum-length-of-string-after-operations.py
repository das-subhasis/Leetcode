#
# @lc app=leetcode id=3223 lang=python3
#
# [3223] Minimum Length of String After Operations
#

# @lc code=start
from collections import Counter
class Solution:
    def minimumLength(self, s: str) -> int:
        c_map = Counter(s)
        length = 0
        for val in c_map.values():
            if val % 2 == 0:
                length += 2
            else:
                length += 1
        return length

# @lc code=end

