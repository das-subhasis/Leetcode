from typing import List

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        n = len(nums)
        prefix_count = [0] * (n + 1)
        prefix_count[0] = 1
        curr_sum = 0
        total = 0
        for num in nums:
            curr_sum += num
            if curr_sum >= goal:
                total += prefix_count[curr_sum - goal]    
            prefix_count[curr_sum] += 1
        
        return total

solution = Solution()
print(solution.numSubarraysWithSum([0,0,0,0,0], 0))
