from collections import deque

class Node:
    def __init__(self, val=0, right=None, left=None):
        self.val = val
        self.right= right
        self.left = left

class Solution:
    def __init__(self):
        self.root = None
        
    def max_depth_bfs(self, root):
        if not root:
            return 0
        
        level = 0
        q = deque([root])
        
        while q:
            for i in range(len(q)):
                node = q.popleft()
                
                if node.left:
                    q.append(node.left)
                    
                if node.right:
                    q.append(node.right)
                    
            level+=1
            
        return level
    
    def max_depth_dfs(self,root):
        if not root:
            return 0
        
        return 1+ max(self.max_depth_dfs(root.left), self.max_depth_dfs(root.right))
                    
        
    def insert(self,value):
        if self.root is None:
            self.root = Node(value)
            
        else:
            self._insert_after(self.root, value)
            
            
    def _insert_after(self, node, value):
        if value < node.val:
            if node.left is None:
                node.left = Node(value)
                
            else:
                self._insert_after(node.left, value)
                
        else:
            if node.right is None:
                node.right = Node(value)
                
            else:
                self._insert_after(node.right, value)
            
        
    def pre_order_bfs(self, root):
        if not root:
            return
         
        print(root.val)
        self.pre_order_bfs(root.left)
        self.pre_order_bfs(root.right)
        
        
    def post_order_bfs(self,root):
        if not root:
            return
        
        self.post_order_bfs(root.left)
        self.post_order_bfs(root.right)
        print(root.val)
            
        
        
        
    def inorder_bfs(self, root):
        if not root:
            return
        
        self.inorder_bfs(root.left)
        print(root.val)
        self.inorder_bfs(root.right)
        
        
new_node = Solution()
new_node.insert(4)
new_node.insert(7)
new_node.insert(9)
new_node.insert(6)
new_node.insert(2)
new_node.insert(3)
new_node.insert(1)

new_node.pre_order_bfs(new_node.root)



        