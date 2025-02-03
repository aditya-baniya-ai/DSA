class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def merge(list1, list2):
        dummyNode = temp = ListNode(-1)
        while list1 and list2:
            if list1.val < list2.val:
                temp.next = list1
                list1 = list1.next
                temp = temp.next 
                
            else:
                temp.next = list2
                list2 = list2.next
                temp = temp.next 
                
        if list1:
            temp.next = list1 
        else:
            temp.next = list2
            
        return dummyNode.next