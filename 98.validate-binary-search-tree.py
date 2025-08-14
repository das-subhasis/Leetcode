#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def traverse(root, lower = float('-inf'), upper = float('inf')):
            if root is None:
                return True
            
            if not (lower < root.val < upper):
                return False
            
            return traverse(root.left, lower, root.val) and traverse(root.right, root.val, upper)
        
        return traverse(root)
# @lc code=end

