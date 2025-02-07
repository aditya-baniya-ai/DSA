class Node:
    def __init__(self, val=0, right=None, left=None):
        self.val = val
        self.right= right
        self.left = left

class Solution:
    def invertTree(self, root):
        if not root:
            return 
        
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root
        