#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        for i, char in enumerate(strs[0]):
            for j in range(1, len(strs)):
                if len(strs[j]) <= i or strs[j][i] != char:
                    return prefix
            prefix += char
        return prefix
# @lc code=end

