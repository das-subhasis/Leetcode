#
# @lc app=leetcode id=122 lang=python3
#
# [122] Best Time to Buy and Sell Stock II
#

# @lc code=start
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        profit = 0
    
        for i in range(1, len(prices)):
            if buy > prices[i]:
                buy = prices[i]
            else:
                profit += (prices[i] - buy)
                buy = prices[i]
        return profit
# @lc code=end

