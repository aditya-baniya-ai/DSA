from typing import Optional
from typing import List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # 'res' will store the final result: a list of levels, each level is a list of node values.
        res = []
        
        # 'q' is a deque (double-ended queue) used for efficient FIFO operations in our BFS traversal.
        q = deque()
        q.append(root)  # Start with the root node in the queue.
        
        # Continue the BFS until there are no more nodes to process.
        while q:
            # 'level' will hold all node values at the current level.
            level = []
            
            # The number of nodes at the current level is fixed by the current length of 'q'.
            # We use 'for i in range(len(q))' to process exactly those nodes.
            for i in range(len(q)):
                # Remove a node from the front of the queue.
                node = q.popleft()
                
                # If the node is not None, process it.
                if node:
                    # Add the node's value to the current level list.
                    level.append(node.val)
                    
                    # Add the node's children (they could be None) to the queue for the next level.
                    q.append(node.left)
                    q.append(node.right)
            
            # Only add non-empty levels to the final result.
            # This check prevents adding an extra empty level when there are trailing None values.
            if level:
                res.append(level)
        
        # Return the level order traversal result.
        return res