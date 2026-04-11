#
# @lc app=leetcode id=224 lang=python3
#
# [224] Basic Calculator
#

# @lc code=start
class Solution:
    def calculate(self, s: str) -> int:
        exp_stk = []
        # remove the whitespaces, only keep the operators and operands in the expression
        s = s.replace(' ', '')
        operators = {'+', '-', '('}
        prev_open = False
        for c in s:
            if c in operators:
                exp_stk.append(c)
                prev_open = c == '('
            if c == ')' and prev_open:
                while prev_open:
                    val = exp_stk.pop()
                    if val == '(':
                        prev_open = False
                    else:
                        

            




        
# @lc code=end

