# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # Define a helper function 'dfs' to perform a depth-first search.
        # This function takes in the current node and the maximum value (maxVal)
        # encountered along the path from the root to this node.
        def dfs(root, maxVal):
            # Base Case: If the current node is None, there are no nodes to count,
            # so return 0.
            if not root:
                return 0
            
            # Check if the current node is "good":
            # A node is "good" if its value is greater than or equal to the maximum value
            # seen so far along the path from the root.
            # If it is good, we count it as 1; otherwise, 0.
            ans = 1 if root.val >= maxVal else 0
            
            # Update maxVal to be the maximum between the current maxVal and the current node's value.
            # This ensures that we carry the maximum value seen so far down to the children.
            maxVal = max(maxVal, root.val)
            
            # Recursively perform DFS on the left subtree and add the number of good nodes.
            ans += dfs(root.left, maxVal)
            # Recursively perform DFS on the right subtree and add the number of good nodes.
            ans += dfs(root.right, maxVal)
            
            # Return the total count of good nodes for the current subtree.
            return ans
        
        # Start the DFS with the root node.
        # The initial maxVal is set to the root's value because the path starts at the root.
        return dfs(root, root.val)