from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_freq = Counter(t)
        sub = ''
        min_len = float('inf')
        formed = 0
        required = len(t_freq)
        left = 0
        n = len(s)
        s_freq = {}
        for right in range(n):
            s_freq[s[right]] = s_freq.get(s[right], 0) + 1

            if s[right] in t_freq and s_freq[s[right]] == t_freq[s[right]]:
                formed += 1
            
            while formed == required:
                window_len = right - left + 1
                if window_len < min_len:
                    min_len = window_len
                    sub = s[left:right + 1]
                
                left_char = s[left]
                s_freq[left_char] -= 1

                if left_char in t_freq and s_freq[left_char] < t_freq[left_char]:
                    formed -= 1

                left += 1
        return sub


