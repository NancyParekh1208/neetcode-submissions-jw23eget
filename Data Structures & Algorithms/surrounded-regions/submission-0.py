class Solution:
    def solve(self, board: List[List[str]]) -> None:

        # Main focus is to find the regions that are considered not surrounded as they 
        # are connected to the border.
        # MARK such regions temporarily as # and later mark all surrounded regions 'O' which did not become # to X.
        # Mark all # back to O.
        ROWS = len(board)
        COLS = len(board[0])

        def capture(r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or board[r][c] != 'O':
                return
            
            board[r][c] = '#'
            capture(r+1,c)
            capture(r-1,c)
            capture(r,c-1)
            capture(r,c+1)

        for i in range(ROWS):
            # check first column
            if board[i][0] == 'O':
                capture(i,0)
            if board[i][COLS-1] == 'O':
                capture(i,COLS-1)
        
        for j in range(COLS):
            # check first row
            if board[0][j] == 'O':
                capture(0,j)
            if board[ROWS-1][j] == 'O':
                capture(ROWS-1, j)
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '#':
                    board[i][j] = 'O'
                    


        