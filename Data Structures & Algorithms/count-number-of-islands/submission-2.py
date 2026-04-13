class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        m = len(grid)
        n = len(grid[0])

        dirs = [[0,1],[1,0],[-1,0],[0,-1]]

        countIslands = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    q = deque()
                    q.append((i,j))
                    while q:
                        # explore neighbors
                        row, col = q.popleft()
                        grid[row][col] = '0'
                        for dr, dc in dirs:
                            newrow = dr+row
                            newcol = dc+col
                            if newrow < 0 or newcol < 0 or newrow >= m or newcol >= n or grid[newrow][newcol] == '0':
                                continue
                            else: 
                                q.append((newrow,newcol))

                    countIslands+=1
        
        return countIslands
