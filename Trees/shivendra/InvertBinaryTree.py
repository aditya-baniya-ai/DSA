from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Base case: if root is None, i.e. root list is empty
        if not root: #root is just the list name
            return None

        # Recursively store the left and right subtrees nodes value
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)

        # Swap the left and right children
        root.left = right
        root.right = left

        # Return the root node
        return root
    
#Input: root = [4,2,7,1,3,6,9]
#Output: [4,7,2,9,6,3,1]