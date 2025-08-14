#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
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
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        queue = deque([root])
        depth = 0
        maxDepth = float('-inf')
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if not node.left and not node.right:
                    maxDepth = max(maxDepth, depth + 1)
                if node.right: queue.append(node.right)
                if node.left: queue.append(node.left)
            depth += 1
        return maxDepth
# @lc code=end

