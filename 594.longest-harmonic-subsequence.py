# Input: nums = [1,3,2,2,5,2,3,7]
# Output: 5
#
# EXP: The longest harmonious subsequence is [3,2,2,2,3].

from collections import Counter
from typing import List
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        max_len = 0

        freq = Counter(nums)
        for num in freq:
            if num - 1 in freq:
                max_len = max(max_len, freq[num] + freq[num - 1])
        return max_len
            
            
