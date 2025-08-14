#
# @lc app=leetcode id=2594 lang=python3
#
# [2594] Minimum Time to Repair Cars
#
import math
from typing import List
# @lc code=start
class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def canRepairAllCars(time):
            repaired = 0
            for rank in ranks:
                repaired += int(math.sqrt((time/rank)))
                if repaired >= cars:
                    return True
            return repaired >= cars
        l, r = 1, min(ranks) * (cars ** 2)
        while l < r:
            mid = (l + r) // 2
            canRepair = canRepairAllCars(mid)

            if canRepair:
                r = mid
            else:
                l = mid + 1
        return l
                
# @lc code=end

