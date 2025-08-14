#
# @lc app=leetcode id=1376 lang=python3
#
# [1376] Time Needed to Inform All Employees
#

# @lc code=start
from collections import defaultdict, deque


class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        manager_map = defaultdict(list)
        for idx, man in enumerate(manager): manager_map[man].append(idx)
        totalTime = 0
        queue = deque([(headID, 0)])
        while queue:
            node, time = queue.popleft()
            totalTime = max(totalTime, time)
            for neighbour in manager_map[node]:
                queue.append((neighbour, time  + informTime[node]))
            
        return totalTime


# @lc code=end

