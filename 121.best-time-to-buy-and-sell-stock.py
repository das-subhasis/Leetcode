#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    """
        Intuition: First we buy the stock on day 1 and roll on throught the subsequent days,
        IF we see that we have a stock next / subs. days less the price than current we buy that 
        For all days we calculate profit based on the stock price of that day.
    """
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = prices[0]

        for i in range(1, len(prices)):
            if buy > prices[i]:
                buy = prices[i]
            profit = max(prices[i] - buy, profit)
        return profit


# @lc code=end

