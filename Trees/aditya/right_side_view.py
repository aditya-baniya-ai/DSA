# we use level order traversal(BFS)
# We start from node and put right nodes first in the queue
# Then we store all elements in a list and add the most right node in ans
# which will be the first element in list

from collections import deque
def right_side_view(root):
    if not root:
        return []
    
    res=[]
    
    q = deque([root])
    
    while q:
        l = []
        n = len(q)
        
        for i in range(len(q)):
            node = q.popleft()
            l.append(node.val)
            
            if node.right:
                q.append(node.right)
                
            if node.left:
                q.append(node.left)
                
        res.append(l[0])
        
    return res