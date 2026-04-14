class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:


        m = len(board)
        n = len(board[0])
        
        def dfs(row, col, index):
            if index == len(word):
                return True
            if (row<0 or col<0 or row>=m or col>=n or word[index]!=board[row][col] or board[row][col] == '#'):
                return False
            board[row][col] = '#'
            res = (dfs(row + 1, col, index + 1) or
                   dfs(row - 1, col, index + 1) or
                   dfs(row, col + 1, index + 1) or
                   dfs(row, col - 1, index + 1))
            board[row][col] = word[index]
            return res
            
            

        for i in range(m):
            for j in range(n):
                if dfs(i,j,0):
                    return True
        return False

        