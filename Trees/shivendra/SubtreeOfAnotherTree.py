from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution: 
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Helper function to check if two trees are the same
        def sameTree(p, q):
            # If both nodes are None, they are considered equal
            if not p and not q:
                return True
            # If one is None and the other is not, trees are not the same
            if (p and not q) or (q and not p):
                return False
            # If values of current nodes are not equal, trees are not the same
            if p.val != q.val:
                return False
            
            # Recursively check the left and right subtrees
            return sameTree(p.left, q.left) and sameTree(p.right, q.right)
        
        # Helper function to traverse the tree and find if subRoot is a subtree
        def hasSubtree(root):
            # If the current node is None, return False
            if not root:
                return False
            # If the current node's tree matches subRoot, return True
            if sameTree(root, subRoot):
                return True
            # Recursively check both left and right subtrees
            return hasSubtree(root.left) or hasSubtree(root.right)

        # Start by checking from the root of the main tree
        return hasSubtree(root)