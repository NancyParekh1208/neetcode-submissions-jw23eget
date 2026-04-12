class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        n = len(cost)
        if n == 0:
            return 0
        if n == 1:
            return cost[0]
        
        memo = [-1]*n

        def dfs(i):
            if i >= n:
                return 0
            if memo[i] != -1:
                return memo[i]
            memo[i] =  cost[i] + min(dfs(i+1), dfs(i+2))  
            return memo[i]  

        return min(dfs(0), dfs(1)) # cost of starting from 0 or 1

        