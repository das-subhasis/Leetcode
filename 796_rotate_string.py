from typing import List

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        n, m = len(s), len(goal)

        if m != n: return False

        for i in range(n):
            k = (i + 1) % n
            rotate = s[k:] + s[:k]
            print(rotate)
            if rotate == goal: return True
        return False

s = "abcde"
goal = "cdeab"
solution = Solution()
print(solution.rotateString(s, goal))


