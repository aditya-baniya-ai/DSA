""" 
    To check if it has a cycle or not, we can move one pointer slow and 
    another fast. It makes sure that if it has not any cycle then slow and 
    fast never met then we return False. Else if they somehow equal each other that 
    means it has a cycle in it
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head):
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

            
        return False