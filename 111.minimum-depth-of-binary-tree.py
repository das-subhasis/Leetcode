#
# @lc app=leetcode id=111 lang=python3
#
# [111] Minimum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        count = 0
        queue = deque([root])
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if (not node.left) and (not node.right):
                    return count + 1
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            count += 1
        return count

        
# @lc code=end

