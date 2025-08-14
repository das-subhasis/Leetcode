#
# @lc app=leetcode id=2244 lang=python3
#
# [2244] Minimum Rounds to Complete All Tasks
#

# @lc code=start
from collections import defaultdict
from typing import List


class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        freq_map = defaultdict(int)
        for num in tasks:
            if num not in freq_map:
                freq_map[num] = 1
                continue
            freq_map[num] += 1
        rounds = 0
        for count in freq_map.values():
            if count == 1:
                return -1  
            if count % 3 == 0:
                rounds += count // 3
            else:
                rounds += count // 3 + 1  

        return rounds

sol = Solution()
print(sol.minimumRounds([66,66,63,61,63,63,64,66,66,65,66,65,61,67,68,66,62,67,61,64,66,60,69,66,65,68,63,60,67,62,68,60,66,64,60,60,60,62,66,64,63,65,60,69,63,68,68,69,68,61]))
# @lc code=end

