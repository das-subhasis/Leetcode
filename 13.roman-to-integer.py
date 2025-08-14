#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_int_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        ans = roman_to_int_map[s[-1]]
        for i in range(len(s) - 2, -1, -1):
            if roman_to_int_map[s[i]] >= roman_to_int_map[s[i + 1]]:
                ans += roman_to_int_map[s[i]]
            else:
                ans -= roman_to_int_map[s[i]]
        return ans
    
sol = Solution()
print(sol.romanToInt('XII'))
# @lc code=end

