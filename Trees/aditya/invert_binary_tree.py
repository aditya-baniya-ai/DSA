        
""""
    Simple solution is if not root return
    then invert binary tree means swapping the value of tree. assign left to right and right to left
    then call recursive function to each side of tree. Should call the same function for both left and right and return node
"""

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
        