from typing import Optional,List
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Define a helper function that validates the BST property for the subtree rooted at 'node'.
        # 'minn' is the lower bound (exclusive) and 'maxx' is the upper bound (exclusive) for the node values.
        def valid(node, minn, maxx):
            # If the current node is None, then by definition it's a valid BST.
            if node is None:
                return True

            # Check if the current node's value violates the BST property:
            # it must be strictly greater than 'minn' and strictly less than 'maxx'.
            if not (minn < node.val < maxx):
                return False

            # Recursively validate the left subtree:
            # All values in the left subtree must be less than the current node's value.
            # Hence, update the upper bound to node.val.
            # Recursively validate the right subtree:
            # All values in the right subtree must be greater than the current node's value.
            # Hence, update the lower bound to node.val.
            return valid(node.left, minn, node.val) and valid(node.right, node.val, maxx)

        # Start the recursion with the entire range of possible values,
        # using negative infinity as the initial lower bound and positive infinity as the initial upper bound.
        return valid(root, float("-inf"), float("inf"))
