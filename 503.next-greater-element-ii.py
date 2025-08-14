#
# @lc app=leetcode id=503 lang=python3
#
# [503] Next Greater Element II
#

# @lc code=start
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        n = len(nums)
        res = [float('-inf')] * n

        for i in range(n-1, -1, -1):
            while stack and stack[-1] <= nums[i]:
                stack.pop()
            
            if stack:
                res[i] = stack[-1]
            stack.append(nums[i])
        i = n - 1
        while stack and stack[0] > nums[i]:
            if res[i] == float('-inf'):
                while stack and stack[-1] <= nums[i]:
                    stack.pop()
                
                if stack:
                    res[i] = stack[-1]
            i -= 1
        res = [val if val != float('-inf') else -1 for val in res]
        return res
# @lc code=end

