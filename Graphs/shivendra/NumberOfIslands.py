from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Initialize the counter for the number of islands.
        num_islands = 0

        # Determine the number of rows and columns in the grid.
        ROWS, COLS = len(grid), len(grid[0])

        # If the grid is empty, return 0 as there are no islands.
        if not grid:
            return 0

        # Define a helper function 'dfs' to perform a depth-first search.
        # This function will "sink" an island by converting all connected '1's (land) to '0's (water).
        def dfs(r: int, c: int):
            # Check if the current cell is out of bounds or already water ('0').
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == '0':
                return None

            # Mark the current cell as visited by setting it to '0'.
            grid[r][c] = '0' #sinking the land by visiting them and setting it to '0'

            # Recursively call dfs on the four adjacent cells (down, up, right, left).
            dfs(r + 1, c)  # Move down.
            dfs(r - 1, c)  # Move up.
            dfs(r, c + 1)  # Move right.
            dfs(r, c - 1)  # Move left.

        # Iterate over every cell in the grid.
        for r in range(ROWS):
            for c in range(COLS):
                # If a cell contains land ('1'), then we've found an island.
                if grid[r][c] == '1':
                    # Increment the island counter.
                    num_islands += 1
                    # Use DFS to "sink" the island, marking all its connected land as water.
                    dfs(r, c)

        # Return the total number of islands found.
        return num_islands
