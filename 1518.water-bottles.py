#
# @lc app=leetcode id=1518 lang=python3
#
# [1518] Water Bottles
#

# @lc code=start
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        totalDrinks = 0
        carryForward = 0
        while numBottles > 0:
            totalDrinks += numBottles
            exchange = ((numBottles + carryForward) // numExchange)
            carryForward = ((numBottles + carryForward) % numExchange)
            numBottles = exchange
        return totalDrinks

sol = Solution()
print(sol.numWaterBottles(15, 4))
# @lc code=end

