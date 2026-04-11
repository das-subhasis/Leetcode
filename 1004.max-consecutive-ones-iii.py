# Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.
from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        longest = 0
        zero = 0
        n = len(nums)

        for right in range(n):
            if nums[right] == 0:
                zero += 1

            while zero > k:
                if nums[left] == 0:
                    zero -= 1
                left += 1
                
            longest = max(longest, right - left + 1)
        return longest 

solution = Solution()
nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
print(solution.longestOnes(nums, k))
