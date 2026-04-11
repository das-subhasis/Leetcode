# Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.
from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0] * n
        stk = []

        for i in range(n):
            while stk and temperatures[i] > temperatures[stk[-1]]:
                pos = stk.pop()
                answer[pos] = i - pos
            stk.append(i)
        return answer
