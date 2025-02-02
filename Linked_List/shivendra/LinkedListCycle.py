def hasCycle(head):
    sett = set() # Hash_set
    curr = head
    while curr:
        if curr in sett: #if cuurent node found in our hashset, means cycle exists
            return True
        sett.add(curr) # add each new node in out hashset
        curr = curr.next #don't forget to update the curr
        
    return False