class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:

        minSorted = ListNode()
        maxSorted = ListNode()
        minTail = minSorted
        maxTail = maxSorted

        current = head
        while current:  
            val = current.val
            
            if val < x:
                minTail.next = current
                minTail = minTail.next
            else:
                maxTail.next = current
                maxTail = maxTail.next
            current = current.next
        
        minSorted = minSorted.next
        maxSorted = maxSorted.next

        minTail.next = maxSorted
        maxTail.next = None

        return minSorted if minSorted else maxSorted

            
