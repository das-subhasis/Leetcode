#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
strs = ["flower","flow","flight"]
print(min(strs, key= lambda x : len(x)))
        
# @lc code=end

