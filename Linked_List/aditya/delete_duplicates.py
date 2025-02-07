class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def deleteDuplicates(self, head):
        temp = head
        
        if not head:
            return
        
        while temp!= None:
            if(temp.val == temp.next.val):
                temp.next = temp.next.next 
            else:
                temp = temp.next 