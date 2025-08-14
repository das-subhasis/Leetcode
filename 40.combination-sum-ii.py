#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#

# @lc code=start
class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        res, sol = [], []
        n = len(candidates)
        candidates.sort()
        def backtrack(i, count):
            if count == target:
                res.append(sol[:])
                return
            
            for j in range(i, n):
                if j > i and candidates[j] == candidates[j - 1]:
                    continue

                if count > target:
                    break
            
                sol.append(candidates[j])
                backtrack(j + 1, count + candidates[j])
                sol.pop()

        backtrack(0, 0)
        return res
sol = Solution()
print(sol.combinationSum2([10,1,2,7,6,1,5], 8))
# @lc code=end

