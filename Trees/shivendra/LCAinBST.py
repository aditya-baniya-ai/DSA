from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution: 
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        # Start the search from the root of the BST.
        curr = root
        
        # Continue the search until the lowest common ancestor is found.
        while curr:
            # If both p and q have values greater than the current node's value,
            # then both nodes are located in the right subtree of the current node.
            if p.val > curr.val and q.val > curr.val:
                curr = curr.right  # Move to the right child to continue the search.
            # If both p and q have values less than the current node's value,
            # then both nodes are located in the left subtree of the current node.
            elif p.val < curr.val and q.val < curr.val:
                curr = curr.left  # Move to the left child to continue the search.
            else:
                # If we reach here, it means:
                # 1. p and q are on different sides of the current node, or
                # 2. One of p or q is equal to the current node.
                # In either case, the current node is the lowest common ancestor.
                return curr

#Time complexity: O(h) where h is the height of the tree, In BST h= logN. Hence, time = O(logN)