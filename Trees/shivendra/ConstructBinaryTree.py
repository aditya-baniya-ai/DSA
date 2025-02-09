from typing import Optional,List
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        #Hack: Make a level order traversal binary tree of [1,2,3,4,5,6,7], then list preorder and inorder elements.
        #Then, write code by seeing what indexes work to be at preorder and inorder
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # If either preorder or inorder is empty, no tree exists, so return None.
        if not preorder or not inorder:
            return None

        # The first element in preorder is the root.
        # For our example, preorder[0] is 1.
        root = TreeNode(preorder[0])
        
        # Find the index of the root in the inorder list.
        # In our example, inorder.index(1) returns 3.
        mid = inorder.index(preorder[0])
        
        # Elements in inorder before index 3 (i.e. [4, 2, 5]) form the left subtree.
        # The corresponding preorder slice for the left subtree is:
        # elements from index 1 to index mid+1 (i.e. preorder[1:4] which is [2, 4, 5]).
        root.left = self.buildTree(preorder[1 : mid + 1], inorder[:mid])
        
        # Elements in inorder after index 3 (i.e. [6, 3, 7]) form the right subtree.
        # The corresponding preorder slice for the right subtree is:
        # the remaining elements after the left subtree (i.e. preorder[4:] which is [3, 6, 7]).
        root.right = self.buildTree(preorder[mid + 1 :], inorder[mid + 1 :])
        
        # Return the constructed tree rooted at 'root'.
        return root