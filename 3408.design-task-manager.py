#
# @lc app=leetcode id=3408 lang=python3
#
# [3408] Design Task Manager
#
import heapq
from typing import List
# @lc code=start
class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        # tasks are list of [userId, taskId, priority]
        self.entry_finder = {}
        self.tasks = []
        for uid, tid, p in tasks:
            entry = (-p, -tid, uid) 
            self.tasks.append(entry)
            self.entry_finder[tid] = (uid, -p)
        heapq.heapify(self.tasks)

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.entry_finder[taskId] = (userId, -priority)
        heapq.heappush(self.tasks, ( -priority, -taskId, userId))

    def edit(self, taskId: int, newPriority: int) -> None:
        uid, _ = self.entry_finder[taskId]
        self.entry_finder[taskId] = (uid, -newPriority)
        new_entry = (-newPriority, -taskId, uid)
        heapq.heappush(self.tasks, new_entry)
    
    def rmv(self, taskId: int) -> None:
        del self.entry_finder[taskId]

    def execTop(self) -> int:
        while self.tasks:
            neg_p, neg_tid, uid = heapq.heappop(self.tasks)
            if -neg_tid in self.entry_finder and self.entry_finder[-neg_tid] == (uid, neg_p):
                del self.entry_finder[-neg_tid]
                return uid
        return -1





# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()
# @lc code=end

