#
# @lc app=leetcode id=1189 lang=python3
#
# [1189] Maximum Number of Balloons
#

# @lc code=start
from collections import defaultdict
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        char_map = defaultdict(int)
        balloon = "balloon"
        for letter in text:
            char_map[letter] += 1
        
        if any(ltr not in char_map for ltr in balloon):
            return 0
        else:
            return min(char_map['b'],
                       char_map['a'],
                       char_map['l'] // 2,
                       char_map['o'] // 2,
                       char_map['n'],
                       )
# @lc code=end

