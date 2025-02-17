from typing import Optional

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # If the input node is None, return None (base case)
        if not node:
            return None

        # Dictionary to map original nodes to their clones.
        # This helps to avoid re-cloning nodes and handles cycles.
        clones = {}

        # Define a helper function for depth-first search (DFS)
        def dfs(node):
            # If this node has already been cloned, return the clone.
            if node in clones:
                return clones[node]
            
            # Create a clone for the current node with the same value,
            # and initialize its neighbor list as empty.
            clone = Node(node.val, [])
            
            # Store the clone in the dictionary before processing neighbors,
            # so that cycles are handled correctly.
            clones[node] = clone
            
            # Iterate over all the neighbors of the original node.
            for nei in node.neighbors:
                # Recursively clone each neighbor and add it to the clone's neighbor list.
                clone.neighbors.append(dfs(nei))
            
            # Return the clone of the current node.
            return clone

        # Start DFS from the given node and return the cloned graph.
        return dfs(node)
