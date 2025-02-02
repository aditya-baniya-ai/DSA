from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Create a dummy node to handle edge cases (like removing first node)
        dummy = ListNode()
        dummy.next = head
        l = r = dummy

        # Move right pointer n steps ahead
        while n > 0:
            r = r.next
            n -= 1
        # Move both pointers until r reaches at the last node
        while r.next:
            r = r.next
            l = l.next

        # Remove the nth node
        l.next = l.next.next

        return dummy.next

