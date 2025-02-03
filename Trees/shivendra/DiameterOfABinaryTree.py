from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:  
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        self.res= 0 # Stores the maximum diameter found
        
        def dfs(root):
            if not root:
                return 0 # Base case: empty tree has depth 0

            # Recursively find depth of left and right subtrees  
            left_depth = dfs(root.left)
            right_depth = dfs(root.right)

            # Update res if current path is the longest found
            self.res = max(self.res, left_depth + right_depth)

            # Return the depth of the current node
            return max(left_depth, right_depth) + 1

        dfs(root) # Start DFS from the root
        return self.res