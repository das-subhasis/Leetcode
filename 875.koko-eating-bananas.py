#
# @lc app=leetcode id=875 lang=python3
#
# [875] Koko Eating Bananas
#

# @lc code=start
import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canEatAll(k):
            hours_spent = sum(-(-pile // k) for pile in piles)
            return hours_spent <= h

        l, r = 1, max(piles)

        while l < r:
            mid = (l + r) // 2
            canEat = canEatAll(mid)

            if canEat:
                r = mid
            else:
                l = mid + 1
        return l
                            
# @lc code=end

