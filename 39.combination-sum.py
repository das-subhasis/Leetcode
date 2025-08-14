#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#

# @lc code=start
from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res, sol = [], []
        n = len(candidates)
        def backtrack(i, count):
            if count == target:
                res.append(sol[:])
                return

            if i == n or count > target:
                return
            
            backtrack(i + 1, count)
            sol.append(candidates[i])
            backtrack(i, count + candidates[i])
            sol.pop()

        backtrack(0, 0)
        return res
    
sol = Solution()
print(sol.combinationSum(candidates = [2,3,6,7], target = 7))
# @lc code=end

