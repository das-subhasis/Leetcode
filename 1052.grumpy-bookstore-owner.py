# There is a bookstore owner that has a store open for n minutes. You are given an integer array customers of length n where customers[i] is the number of the customers that enter the store at the start of the ith minute and all those customers leave after the end of that minute.
#
# During certain minutes, the bookstore owner is grumpy. You are given a binary array grumpy where grumpy[i] is 1 if the bookstore owner is grumpy during the ith minute, and is 0 otherwise.
#
# When the bookstore owner is grumpy, the customers entering during that minute are not satisfied. Otherwise, they are satisfied.
#
# The bookstore owner knows a secret technique to remain not grumpy for minutes consecutive minutes, but this technique can only be used once.
#
# Return the maximum number of customers that can be satisfied throughout the day.
from typing import List
class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        # n - amount of time store remains open
        # customers - n customers 
        # customers[i] - no. of customers at ith min who enter/exit the shop
        # grumpy[i] - shows the owner is normal (0) / grumpy (1) at ith min
        # grumpy(1) - customer not satisfied -> grumpy(0) - customers are satisfied
        # `minutes` - total consecutive minutes owner can not be grumpy. But can be done exactly once.

        n = len(grumpy)
        base_satisfaction = sum(customers[i] if grumpy[i] == 0 else 0 for i in range(n))
        customer_win = sum(customers[i] if grumpy[i] == 1 else 0 for i in range(n))
        max_customer_win = customer_win

        for i in range(minutes, n):
            customer_win += customers[i] if grumpy[i] == 1 else 0
            customer_win -= customers[n - i - 1] if grumpy[i] == 1 else 0
            max_customer_win = max(max_customer_win, customer_win)
        return base_satisfaction + max_customer_win

customers = [1,0,1,2,1,1,7,5]
grumpy = [0,1,0,1,0,1,0,1]
minutes = 3
solution = Solution()
print(solution.maxSatisfied(customers, grumpy, minutes))
