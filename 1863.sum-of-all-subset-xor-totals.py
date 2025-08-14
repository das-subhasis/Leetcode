#
# @lc app=leetcode id=1863 lang=python3
#
# [1863] Sum of All Subset XOR Totals
#

# @lc code=start
class Solution:
    def subsetXORSum(self, nums: list[int]) -> int:
        n = len(nums)
        xorTotal, sol = [0], []

        def backtrack(i):
            if i == n:
                if not sol:
                    return
                res = sol[0]
                for j in range(1, len(sol)):
                    res ^= sol[j]
                xorTotal[0] += res
                return
            
            sol.append(nums[i])
            backtrack(i + 1)
            sol.pop()

            backtrack(i + 1)
        backtrack(0)
        return xorTotal[0]

sol = Solution()
print(sol.subsetXORSum([1,3]))      
# @lc code=end

