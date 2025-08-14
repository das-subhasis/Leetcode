#
# @lc app=leetcode id=3394 lang=python3
#
# [3394] Check if Grid can be Cut into Sections
#

# @lc code=start
from typing import List
class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        # check for x directions
        hz = [[rect[0], rect[2]] for rect in rectangles]
        hz.sort()
        res1 = []
        for index in range(1, len(hz)):
            if hz[index - 1][1] > hz[index][0]:
                hz[index][0] = min(hz[index - 1][0], hz[index][0])
                hz[index][1] = max(hz[index - 1][1], hz[index][1])
            else:
                res1.append([hz[index - 1][0], hz[index - 1][1]])
                if len(res1) == 2: return True
        res1.append(hz[-1])
        # check for y direction
        vt = [[rect[1], rect[3]] for rect in rectangles]
        vt.sort()
        res2 = []
        for index in range(1, len(vt)):
            if vt[index - 1][1] > vt[index][0]:
                vt[index][0] = min(vt[index - 1][0], vt[index][0])
                vt[index][1] = max(vt[index - 1][1], vt[index][1])
            else:
                res2.append([vt[index - 1][0], vt[index - 1][1]])
                if len(res2) == 2: return True
        res2.append(vt[-1])
        # if either in x or y return True else False
        return len(res1) >= 3 or len(res2) >= 3

sol = Solution()
print(sol.checkValidCuts(
    4,
    [[0,0,1,4],[1,0,2,3],[2,0,3,3],[3,0,4,3],[1,3,4,4]]
))
# @lc code=end

