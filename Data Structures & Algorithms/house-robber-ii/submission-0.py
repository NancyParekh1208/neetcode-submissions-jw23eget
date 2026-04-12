class Solution:
    def rob(self, nums: List[int]) -> int:

        n = len(nums)
        if n == 0:
            return 0
        elif n == 1:
            return nums[0]
        
        memo = [[-1]* 2 for _ in range(n)]

        def dfs(index, flag):
            if index >= n or (flag and index == n-1):
                return 0
            if memo[index][flag] != -1:
                return memo[index][flag]
            skiphouse = dfs(index + 1, flag) # flag remains same
            considerhouse = nums[index] + dfs(index + 2, flag or index == 0)
            memo[index][flag] = max(skiphouse, considerhouse)
            return memo[index][flag]

        
        return max(dfs(0,True), dfs(1, False))
        