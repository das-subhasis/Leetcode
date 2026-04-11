#
# @lc app=leetcode id=383 lang=python3
#
# [383] Ransom Note
#

# @lc code=start
from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_map = Counter(magazine)
        if len(magazine) < len(ransomNote): return False
        for letter in ransomNote:
            if magazine_map[letter] > 0:
                magazine_map[letter] -= 1
            else:
                return False
        return True
# @lc code=end

