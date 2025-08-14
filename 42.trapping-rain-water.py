#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        LMAX, RMAX = height[l], height[r]
        res = 0
        while l < r:
            if LMAX < RMAX:
                l += 1
                LMAX = max(LMAX, height[l])
                res += LMAX - height[l]
            else:
                r -= 1
                RMAX = max(RMAX, height[r])
                res += RMAX - height[r]
        return res
# @lc code=end

