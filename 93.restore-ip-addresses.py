#
# @lc app=leetcode id=93 lang=python3
#
# [93] Restore IP Addresses
#

# @lc code=start
class Solution:
    def restoreIpAddresses(self, s: str) -> list[str]:
        
        res = []
        n = len(s)
        def backtrack(i, dots, currIp):
            if dots == 4 and i == n:
                res.append(currIp[:-1])
                return
            
            if dots > 4:
                return
            
            for j in range(i, min(i + 3, n)):
                if int(s[i:j + 1]) < 256 and (i == j or s[i] != '0'):
                    backtrack(j + 1, dots + 1, currIp + s[i:j + 1] + ".")
        backtrack(0, 0, "") 
        return res
# @lc code=end

