#
# @lc app=leetcode id=38 lang=python3
#
# [38] Count and Say
#

# @lc code=start
class Solution:
    def getRLE(self, s):
        freq_map = []
        ans = [s[0], 1]
        prev = s[0]
        for i in range(1, len(s)):
            if prev == s[i]:
                ans[1] += 1
            else:
                freq_map.append(ans)
                ans = [s[i], 1]
                prev = s[i]
        freq_map.append(ans)
        new_s = ""
        for char, freq in freq_map:
            new_s += str(freq) + char
        return new_s


    def countAndSay(self, n: int) -> str:
        ans = None
        def countSay(n):
            nonlocal ans
            if n == 1:
                ans = ["1"]
                return
            
            countSay(n - 1)
            ans[0] = self.getRLE(ans[0])
        countSay(n)
        return ans[0]
        
sol = Solution()
print(sol.countAndSay(4))
# @lc code=end

