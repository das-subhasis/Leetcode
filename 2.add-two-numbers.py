#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        c1, c2 = l1, l2
        sum_, carry = 0, 0
        head = ListNode(0)
        current = head
        while c1 or c2 or carry:
            val1 = c1.val if c1 else 0
            val2 = c2.val if c2 else 0

            sum_ = val1 + val2 + carry
            carry = sum_ // 10

            newNode = ListNode(sum_ % 10)
            current.next = newNode
            current = current.next  
            if c1: c1 = c1.next
            if c2: c2 = c2.next
        return head.next

# @lc code=end

