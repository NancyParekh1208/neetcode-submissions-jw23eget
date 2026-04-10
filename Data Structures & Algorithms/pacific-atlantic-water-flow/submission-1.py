class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        m = len(heights)
        n = len(heights[0])
        pac, atl = set(),set()

        dirs = [[0,1],[1,0],[-1,0],[0,-1]]

        def dfs(row, col, visit, prevHeight):
            #need to move in increasing order
            if ((row,col) in visit or row < 0 or col < 0 or row == m or col == n or heights[row][col] < prevHeight):
                return
            visit.add((row,col))
            for dr, dc in dirs:
                dfs(row +dr, col +dc, visit, heights[row][col])

        for c in range(n):
            dfs(0,c,pac,heights[0][c]) # top row
            dfs(m-1,c,atl,heights[m-1][c]) # botton row
        
        for r in range(m):
            dfs(r,0, pac, heights[r][0]) # left side
            dfs(r,n-1,atl,heights[r][n-1]) # right side
        
        res = []
        for r in range(m):
            for c in range(n):
                if (r,c) in pac and (r,c) in atl:
                    res.append((r,c))
        
        return res
                    