class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def deleteDuplicates(self, head):
        temp = prev = dummyNode = head
        
        if not head:
            return
        
        while (temp is not None):
            if (temp.val == prev.val):
                temp = temp.next 
                
            else:
                prev.next = temp
                prev = temp
                
        prev.next = None
        
        return dummyNode