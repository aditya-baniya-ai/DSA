from typing import List

class Solution:
    def pacificAtlantic(self, Heights: List[List[int]]) -> List[List[int]]:
        # Get the number of rows and columns in the grid.
        rows, cols = len(Heights), len(Heights[0])
        
        # Initialize sets to keep track of cells that can reach each ocean.
        # 'pacific' will store coordinates that can reach the Pacific (top/left borders).
        # 'atlantic' will store coordinates that can reach the Atlantic (bottom/right borders).
        pacific, atlantic = set(), set()
        
        # Define a helper DFS function to mark cells reachable from a given starting point.
        # r, c: current cell coordinates.
        # visited: a set to store cells (as tuples) that have been reached.
        # prevHeight: the height of the previous cell to ensure water can flow properly.
        def dfs(r: int, c: int, visited: set, prevHeight: int):
            # If the current cell is out of bounds, or if its height is less than
            # the previous cell (water flows from higher/equal to lower/equal), or
            # if it has already been visited in this DFS, then return immediately.
            if (r < 0 or c < 0 or r == rows or c == cols or prevHeight > Heights[r][c]
                or (r, c) in visited):
                return
            
            # Mark the current cell as visited by adding its coordinates to the set.
            visited.add((r, c))
            
            # Recursively call dfs for the four adjacent cells, using the current cell's
            # height as the new reference height.
            dfs(r + 1, c, visited, Heights[r][c])  # Down
            dfs(r - 1, c, visited, Heights[r][c])  # Up
            dfs(r, c + 1, visited, Heights[r][c])  # Right
            dfs(r, c - 1, visited, Heights[r][c])  # Left
        
        # Start DFS from the border cells for both oceans.
        # For the Pacific Ocean, start from the top row and left column.
        for c in range(cols):
            dfs(0, c, pacific, Heights[0][c])          # Top border (first row)
            dfs(rows - 1, c, atlantic, Heights[rows - 1][c])  # Bottom border (last row)
        for r in range(rows):
            dfs(r, 0, pacific, Heights[r][0])          # Left border (first column)
            dfs(r, cols - 1, atlantic, Heights[r][cols - 1])  # Right border (last column)
        
        # Initialize result list.
        res = []
        
        # For every cell in the grid, check if it can reach both oceans.
        # If so, add its coordinates to the result list.
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pacific and (r, c) in atlantic:
                    res.append([r, c])
        
        # Return the list of coordinates that can reach both oceans.
        return res
