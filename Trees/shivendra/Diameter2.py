from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:  
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Variable to store the largest diameter found, we use [0] as list to refer to the same
        #global variable, self. or nonlocal largest_diameter can also be used inside helper func
        # Using a list to allow modification within nested function
        maxD = [0]  
        
        def height(root):
            if not root:
                return 0  # Base case: If node is None, its height is 0
            
            # Recursively get the height of the left and right subtrees
            left_height = height(root.left)
            right_height = height(root.right)
            
            # Calculate the diameter through this node
            diameter = left_height + right_height
            
            # Update the largest diameter found so far
            # Or use nonlocal largest_diameter
            maxD[0] = max(maxD[0], diameter)
            
            # Return the height of the current node
            return max(left_height, right_height) + 1
        
        height(root)  # Start the recursive process
        return maxD[0]  # Return the maximum diameter found