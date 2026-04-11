class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        freq_map = {}
        left = 0
        maxFreq = 0

        for right in range(len(s)):
            # update the frequency of the character in the current window
            freq_map[s[right]] = freq_map.get(s[right], 0) + 1
            maxFreq = max(maxFreq, freq_map[s[right]])

            while (right - left + 1) - maxFreq > k:
                left += 1

            longest = max(longest, right - left + 1)

        return longest

solution = Solution()
print(solution.characterReplacement("ABAB", 2))

