class ListNode:
 def __init__(self, val=0, next=None):
     self.val = val
     self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 0 or head == None or head.next == None:
            return head

        # two pointers default solution

        n = 0
        current = head
        tail = head
        while tail.next:
            n += 1
            tail = tail.next

        k = k % n


        if k == 0:
            return head


        rotateSteps = n - k - 1
        new_tail = head
        for _ in range(rotateSteps):
            new_tail = new_tail.next

        new_head = new_tail.next

        tail.next = head

        new_tail.next = None

        # Single pass method with slow and fast pointers:
        
        # slow = head
        # fast = head
        #
        # n = 0
        # current = head
        # while current:
        #     n += 1
        #     current = current.next
        #
        # k = k % n
        # if k == 0:
        #     return head
        #
        # for _ in range(k):
        #     fast = fast.next
        #
        # while fast.next:
        #     fast = fast.next
        #     slow = slow.next
        #
        # new_head = slow.next
        # new_tail = slow
        # new_tail.next = None
        # fast.next = head
        
        return new_head

