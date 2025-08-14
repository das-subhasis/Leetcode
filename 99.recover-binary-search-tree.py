#
# @lc app=leetcode id=99 lang=python3
#
# [99] Recover Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        res = []
        def searchTree(root):
            if not root:
                return
            searchTree(root.left)
            res.append(root)
            searchTree(root.right)
        searchTree(root)
        sorted_res = sorted(res, key = lambda x: x.val)
        for i in range(len(res)):
            if res[i].val != sorted_res[i].val:
                res[i].val, sorted_res[i].val = sorted_res[i].val, res[i].val
                break
        return root  

# @lc code=end

