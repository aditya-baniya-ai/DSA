from typing import Optional,List
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = []  # This list will store all node values in in-order (sorted order for a BST).
        
        def dfs(node):
            if not node:
                return None
            # Recursively traverse the left subtree.
            dfs(node.left)
            
            # Use 'nonlocal' so we can modify the 'ans' list defined in the outer function.
            nonlocal ans
            ans.append(node.val)  # Append the current node's value.
            
            # Recursively traverse the right subtree.
            dfs(node.right)
            return ans
        
        # Start in-order DFS traversal from the root.
        ansList = dfs(root)
        # The kth smallest element is at index k-1 (since list indices start at 0).
        return ansList[k-1]
