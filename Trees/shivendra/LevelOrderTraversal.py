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
        # If the tree is empty, return an empty list immediately.
        if root is None:
            return []
        
        # Initialize an empty list 'ans' to store the values of each level.
        ans = []
        # Initialize a queue using deque and add the root node.
        # This queue will help us perform a level order traversal (BFS).
        q = deque([root])
        
        # Continue processing while there are nodes in the queue.
        while q:
            # 'level' will store all node values at the current level.
            level = []
            # The number of nodes at the current level is determined by the current length of 'q'.
            # We iterate exactly that many times to process each node at this level.
            for i in range(len(q)):
                # Remove the node from the front of the queue.
                node = q.popleft()
                # Append the value of the current node to the level list.
                level.append(node.val)
                # If the current node has a left child, add it to the queue for the next level.
                if node.left:
                    q.append(node.left)
                # If the current node has a right child, add it to the queue for the next level.
                if node.right:
                    q.append(node.right)
            # After processing all nodes at the current level, add the level list to our answer.
            ans.append(level)
        
        # Return the final list containing each level's node values.
        return ans