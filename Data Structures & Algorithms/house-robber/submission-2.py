class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        total = 0
        if n == 0:
            return total
        memo = [-1]*n
        def calcTotal(index):
            if index >= n:
                return 0
            if memo[index] != -1:
                return memo[index]
            
            
            # rob current house
            memo[index] = max(nums[index] + calcTotal(index+2), calcTotal(index+1))
            return memo[index]

        return calcTotal(0)