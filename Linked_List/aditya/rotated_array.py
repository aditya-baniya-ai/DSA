class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def rotate(self,head, k):
        if not head:
            return None
        
        count = 1
        temp = head
        
        while temp.next:
            temp = temp.next 
            count +=1
            
        k = k % count
        temp.next = head
        
        for _ in range(count - k):
            temp = temp.next 
            
        new_node = temp.next 
        temp.next = None
        
        return new_node
        
        
        