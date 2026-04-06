class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        islands = 0
        dirs = [[0,1],[1,0],[-1,0],[0,-1]]
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            if (r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == '0'):
                return 
            
            grid[r][c] = '0'
            for dr, dc in dirs:
                dfs(r+dr, c+dc) 
        

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1': #island
                    dfs(r,c) # finds all the connected 1's of the island
                    islands+=1
        
        return islands

        