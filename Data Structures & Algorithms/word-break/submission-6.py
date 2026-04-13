class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        wordSet = set(wordDict) # create hashset
        memo = {}
      
        def dfs(i):
        
            if i in memo:
                return memo[i]
            if i == n:
                return True
            for j in range(i,n):
                if s[i:j+1] in wordSet:
                    if dfs(j+1):
                        memo[i] = True
                        return True
            memo[i] = False
            return False
        
        return dfs(0)