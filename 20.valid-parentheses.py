#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        sym_map = {'}' : '{', ']' : '[', ')' : '('}
        stk = []

        for i in range(len(s)):
            if s[i] in sym_map:
                if stk and stk[-1] == sym_map[s[i]]:
                    stk.pop()
                else:
                    return False
            else:
                stk.append(s[i])

        return False if stk else True
# @lc code=end

