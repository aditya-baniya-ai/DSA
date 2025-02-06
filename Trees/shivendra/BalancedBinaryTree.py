from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:  
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        ans = True

        def dfs(root):
            if not root:
                return 0
            left_height = dfs(root.left)
            right_height = dfs(root.right)

            if abs(left_height - right_height) > 1: #Unbalanced found, false and exit
                nonlocal ans
                ans = False
                return 0 #ends the program

            return max(left_height, right_height) +1 #height of the current node

        dfs(root) #Start DFS traversal
        return ans