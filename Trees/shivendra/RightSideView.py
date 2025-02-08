from collections import deque
from typing import Optional
from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
       # If the tree is empty, return an empty list.
        if not root:
            return []
        
        # Initialize a queue (FIFO) for level order traversal.
        q = deque([root])
        # This list will store the rightmost node's value at each level.
        ans = []
        
        # Process the tree level by level.
        while q:
            # 'rightSide' will keep track of the last node we process at the current level.
            rightSide = None
            # The number of nodes at the current level.
            qLen = len(q)
            
            # Process all nodes at the current level.
            for i in range(qLen):
                # Pop the first node in the queue.
                node = q.popleft()
                # Update rightSide to the current node.
                # Because we process nodes from left to right,
                # the last node processed in the loop is the rightmost node.
                rightSide = node
                
                # If the current node has a left child, add it to the queue.
                if node.left:
                    q.append(node.left)
                # If the current node has a right child, add it to the queue.
                if node.right:
                    q.append(node.right)
            
            # After processing the current level, append the value of the rightmost node.
            ans.append(rightSide.val)
        
        # Return the list of rightmost node values for each level.
        return ans