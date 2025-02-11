def same_tree(p,q):
    if not p or not q:
        return p==q
    
    
    return (p.val ==q.val and same_tree(p.left, q.left) and same_tree(p.right, q.right))
        