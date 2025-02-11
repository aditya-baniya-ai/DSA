def balanced(root):
    return (height(root) >= 0)

def height(node):
    if not node:
        return
    
    left = height(node.left)
    right = height(node.right)
    
    if left <0 or right <0 or abs(right-left) >1:
        return -1
    
    return max(left,right)+1