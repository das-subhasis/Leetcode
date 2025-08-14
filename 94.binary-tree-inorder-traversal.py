#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def traverse(root, store):
            if root == None:
                return
            traverse(root.left, store)
            store.append(root.val)
            traverse(root.right, store)
        
        store = []
        traverse(root, store)
        return store
# @lc code=end

