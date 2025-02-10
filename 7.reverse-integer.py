#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        num = int(str(x)[::-1]) if x >= 0 else -1* int(str(x)[1:][::-1])
        if x == 0:
            return 0
        elif -2**31 <= num <= 2**31:
            return num
        else:
            return 0


# @lc code=end

