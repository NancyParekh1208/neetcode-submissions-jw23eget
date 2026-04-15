class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        dp = [[-1]*n for _ in range(m)] # m rows and n cols
        def dfs(i,j) -> int:

            if i == m-1 and j == n-1:
                return 1 # 1 way to get here
            
            if i >= m or j >= n:
                return 0 # not a path
            
            if dp[i][j] != -1:
                return dp[i][j] # stop the recursion here itself and use dp number of ways

            dp[i][j] = dfs(i+1, j) + dfs(i, j+1)
            return dfs(i+1, j) + dfs(i, j+1)

        ways = dfs(0,0)
        return ways