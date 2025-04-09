def isValidSudoku(self, board):
        #rows
        for r in range (9):
            seen = set()
            for c in range(9):
                item = board[r][c]
                if item in seen:
                    return False
                elif item != '.':
                    seen.add(item)
        #cols
        for r in range (9):
            seen = set()
            for c in range(9):
                item = board[c][r]
                if item in seen:
                    return False
                elif item != '.':
                    seen.add(item)
        #squares
        squares = [(0,0), (0,3),(0,6),
        (3,0),(3,3), (3,6),
        (6,0), (6,3), (6,6)]
        
        for i, j in squares:
            seen = set()
            for r in range(i,i+3):
                for c in range(j,j+3):
                    item = board[r][c]
                    if item in seen:
                        return False
                    elif item != ".":
                        seen.add(item)
        return True