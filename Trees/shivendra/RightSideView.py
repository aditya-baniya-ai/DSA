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
        res = []
        q = deque([root])

        while q:
            rightSide = None
            qLen = len(q)

            for i in range(qLen):
                node = q.popleft()
                if node:
                    # Update rightSide with the current node
                    rightSide = node  
                    # Append left and right children to the queue
                    q.append(node.left)
                    q.append(node.right)
            # After processing the level, rightSide holds the last non-None node seen,
            # which is the rightmost node at that level.
            if rightSide:
                res.append(rightSide.val)
        return res
