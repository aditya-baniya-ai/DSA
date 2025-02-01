def mergeTwoLists(list1, list2):
        
    dummy = ListNode() #pointer to store the address of first node
    curr = dummy

    while list1 and list2:
        if list1.val < list2.val:
            curr.next = list1
            list1 = list1.next #update list1
        else:
            curr.next = list2
            list2 = list2.next #update list2

        curr = curr.next # update curr
    
    curr.next = list1 or list2 # append the rest of the remainings of the list

    return dummy.next
