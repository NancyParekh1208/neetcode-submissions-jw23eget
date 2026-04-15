class Solution:
    def climbStairs(self, n: int) -> int:

        nums = [0]*(n+1)
        if n == 0:
            return 0
        if n == 1:
            return 1
        nums[1] = 1
        nums[2] = 2
        for i in range(3,n+1):
            nums[i] = nums[i-1] + nums[i-2] 

        return nums[n]
        