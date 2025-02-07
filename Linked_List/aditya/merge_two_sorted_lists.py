""" 
    we used dummy node concept. We make a new node with value -1
    then we compare the first element of both linked lists and take the smaller value and point the dummyNode to it
    then we move the list1 or list2 to next node
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def merge(list1, list2):
        dummyNode = temp = ListNode(-1)
        while list1 and list2:
            if list1.val < list2.val:
                temp.next = list1 # dummyNode pointing to the smaller value node
                list1 = list1.next # moving the linked list to next node
                temp = temp.next # moving th dummyNode also to next node
                
            else:
                temp.next = list2
                list2 = list2.next
                temp = temp.next 
                
        if list1:
            temp.next = list1 
        else:
            temp.next = list2
            
        return dummyNode.next