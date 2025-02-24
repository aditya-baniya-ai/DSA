class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def binaryTreePaths(self, root):
        if not root:
            return []
        
        result = []
        
        def dfs(node, path):
            if not node:
                return
            
            path.append(str(node.val))
            if not node.right and not node.left:
                result.append("->".join(path))
                
            else:
                dfs(node.left, path)
                dfs(node.right, path)
                
            #backtracking
            path.pop()
            
        dfs(root, [])
        return result
    