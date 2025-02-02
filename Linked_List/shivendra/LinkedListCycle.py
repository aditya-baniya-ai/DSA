def hasCycle(head):
    sett = set() # Hash_set
    curr = head
    while curr:
        if curr in sett: #if cuurent node found in our hashset, means cycle exists
            return True
        sett.add(curr) # add each new node in out hashset
        curr = curr.next #don't forget to update the curr
        
    return False

#Can also be done using fast and slow pointers
'''
    fast, slow = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

'''
        