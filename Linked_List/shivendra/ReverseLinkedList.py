def reverseList(head):
    p = None #p=prev, c= curr, t= temp
    c = head
    
    while c:
        t = c.next
        c.next = p
        p = c
        c = t
    return p