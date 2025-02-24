from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # Get the dimensions of the board.
        rows, cols = len(board), len(board[0])
        
        # Define a DFS function to "mark" (or "sink") the connected 'O's.
        def dfs(r, c):
            # If the current position is out of bounds or the cell is not 'O', return.
            if r < 0 or c < 0 or r == rows or c == cols or board[r][c] != 'O':
                return
            
            # Mark the cell as 'T' (temporary) to indicate it is connected to the border.
            board[r][c] = 'T'
            
            # Explore all four adjacent directions.
            dfs(r + 1, c)  # Down
            dfs(r - 1, c)  # Up
            dfs(r, c + 1)  # Right
            dfs(r, c - 1)  # Left
        
        # Start DFS from all 'O's on the border.
        # Only cells on the border (first/last row or first/last column) can remain 'O'
        # if they're not captured.
        for r in range(rows):
            for c in range(cols):
                # Check if the cell is on the border and is 'O'.
                if board[r][c] == 'O' and (r in [0, rows - 1] or c in [0, cols - 1]):
                    dfs(r, c)
        
        # After DFS, all 'O's connected to the border are marked as 'T'.
        # Now, flip the remaining 'O's (which are fully surrounded) to 'X'
        # and revert the temporary markers 'T' back to 'O'.
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'  # Flip surrounded 'O' to 'X'.
                elif board[r][c] == 'T':
                    board[r][c] = 'O'  # Revert the temporary marker back to 'O'.
