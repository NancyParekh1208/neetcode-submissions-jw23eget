class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        n = len(coins)
        dp = [amount+1] * (amount+1) # amount of coins needed to make index amount of money
        dp[0] = 0 # Base case: To make amount zero we need zero coins

        for a in range(1, amount+1):
            for c in coins:
                if a-c>=0:
                    dp[a] = min(dp[a], 1 + dp[a-c])
        
        return dp[amount] if dp[amount] != amount+1 else -1