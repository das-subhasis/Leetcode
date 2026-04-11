# Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

from typing import List


class Solution:

    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stk = []
        maxArea = float('-inf')

        for i in range(n):
            area = 0
            while stk and heights[i] < heights[stk[-1]]:
                pos = stk.pop()
                area += (i - pos + 1) * heights[i]
            stk.append(i)
            maxArea = max(maxArea, area)
        return maxArea

solution = Solution()
print(solution.largestRectangleArea([2,1,5,6,2,3]))

