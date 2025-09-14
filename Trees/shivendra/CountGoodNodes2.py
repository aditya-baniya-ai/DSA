# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # Counter to keep track of how many "good nodes" we find
        count = 0

        def dfs(node, maxval):
            # Base case: if the node is None, stop recursion
            if not node:
                return None

            nonlocal count  # allow modification of count defined outside

            # A "good node" is one whose value is >= max value on the path so far
            if node.val >= maxval:
                count += 1   # increment good node count
                # Update maxval since this node becomes the new maximum
                maxval = node.val  

            # Recurse on left subtree
            dfs(node.left, maxval)
            # Recurse on right subtree
            dfs(node.right, maxval)

        # Start DFS with root, initial max value is root's value
        dfs(root, root.val)

        return count
    #Time: O(N), Space: O(H)