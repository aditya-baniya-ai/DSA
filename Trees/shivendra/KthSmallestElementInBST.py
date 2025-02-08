# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional,List
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # 'count' is initialized to k and will be decremented as we traverse nodes.
        # It represents the number of nodes left to process until we reach the kth smallest.
        count = k
        
        # 'ans' will store the kth smallest element's value once it is found.
        ans = 0
        
        # Define a helper function for an in-order DFS traversal.
        # In a BST, in-order traversal processes nodes in increasing order.
        def dfs(node):
            # Base case: If the current node is None, simply return.
            if not node:
                return
            
            # Traverse the left subtree first (in-order: left -> root -> right).
            dfs(node.left)
            
            # Declare that we are using the nonlocal variables 'count' and 'ans'
            # so that changes made here persist outside the current function scope.
            nonlocal count, ans
            
            # If 'count' is 1, it means the current node is the kth smallest,
            # so we update 'ans' with the current node's value.
            if count == 1:
                ans = node.val
                
            # Decrement 'count' because we've processed one more node.
            count -= 1
            
            # Traverse the right subtree.
            dfs(node.right)
            
            # Return the kth smallest element value (this will propagate up after found).
            return ans

        # Start the in-order DFS traversal from the root.
        return dfs(root)
