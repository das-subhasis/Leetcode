#
# @lc app=leetcode id=1249 lang=python3
#
# [1249] Minimum Remove to Make Valid Parentheses
#

# @lc code=start
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stk = []
        n = len(s)
        res = ""
        for i in range(n):
            if s[i] == '(':
                stk.append(s[i])
                res += s[i]
            elif s[i] == ')':
                if stk and stk[-1] == '(':
                    stk.pop()
                    res+= s[i]
            else:
                res += s[i]
        
        return res
    
# @lc code=end

