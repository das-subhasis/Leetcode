from typing import List
class Solution:
 
    def reverse(self, num: int) -> int:
        rev = int(str(num)[::-1].lstrip('0'))
        return rev

    def minMirrorPairDistance(self, nums: List[int]) -> int:
        mirror = {}
        n = len(nums)
        minDistance = float('inf')
        
        for j in range(n):
            rev = self.reverse(nums[j])
            if nums[j] in mirror:
                minDistance = min(minDistance, j - mirror[nums[j]])
            
            mirror[rev] = j
        
        return -1 if minDistance == float('inf') else minDistance

solution = Solution()
print(solution.minMirrorPairDistance([9, 9]))