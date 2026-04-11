#
# @lc app=leetcode id=904 lang=python3
#
# [904] Fruit Into Baskets
#

from typing import List
from collections import Counter
# @lc code=start
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        fruits_map = dict()

        start = 0
        total = float('-inf')

        for end in range(fruits):
            if fruits[end] not in fruits_map:
                fruits_map[fruits[end]] = 0
            fruits_map[fruits[end]] += 1

            if len(fruits_map) > 2:
                fruits_map[fruits[start]] -= 1
                if fruits_map[fruits[start]] == 0:
                    del fruits_map[fruits[start]]
                start += 1
        
            if len(fruits_map) < 2:
                total = max(end - start + 1, total)
        return total






# @lc code=end

