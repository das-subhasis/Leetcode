from collections import defaultdict
class Solution:

    def longestSubstringWithoutRepeat(self, text: str):
        freq_map = defaultdict(int)
        longest = 0
        left = 0
        for right in range(len(text)):
            
            freq_map[text[right]] += 1

            while freq_map[text[right]] > 1:
                freq_map[text[left]] -= 1
                left += 1

            longest = max(longest, right - left + 1)
        return longest

    def longestSubstringWithKDistChar(self, s: str, k: int):
        freq_map = {}
        longest = 0
        left = 0

        for right in range(len(s)):
            freq_map[s[right]] = freq_map.get(s[right], 0) + 1

            while len(freq_map) > k:
                freq_map[s[left]] -= 1
                if freq_map[s[left]] == 0:
                    del freq_map[s[left]]
                left += 1 
            longest = max(longest, right - left + 1)
        return longest

solution = Solution()
print(solution.longestSubstringWithKDistChar("abba", 1))


