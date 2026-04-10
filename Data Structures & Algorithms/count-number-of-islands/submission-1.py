class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        m = len(grid)
        n = len(grid[0])
        islands = 0

        dirs = [[0,1],[1,0],[-1,0],[0,-1]]

        def dfs(row, col):
            if row < 0 or col < 0 or row >= m or col>= n or grid[row][col] == '0':
                return
            grid[row][col] = '0' # mark as visited
            for dr, dc in dirs:
                newrow = dr + row
                newcol = dc + col

                dfs(newrow,newcol) 

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    dfs(i,j)
                    islands+=1

        return islands   
