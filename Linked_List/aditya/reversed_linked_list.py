class ListNode:
    def __init__(self,val,next=None):
        self.val = val
        self.next = next

    def reverseList(head):
        prev = None
        temp = head
        
        while temp!=None:
            front = temp.next  # store next node before modifying
            temp.next = prev  # reverse the link
            prev = temp # move prev forward
            temp = front # move temp forward
            
        return prev     # return new head
    
    def append(self,num):
        temp = self
        while temp.next is not None:
            temp = temp.next
        temp.next = ListNode(num)
    
    def traversal(self):
        temp = self
        while temp is not None:
            print(temp.val,end = "->")
            temp = temp.next
            
        print("None")
            
            
head = ListNode(4)
head.append(5)
head.append(6)
head.traversal()
    
    