class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Kadane's algorithm

        n = len(nums)
        maxSum = nums[0]
        currSum = nums[0]
        if n == 1:
            return currSum
        for i in range(1, n):
            
            currSum = currSum + nums[i]
            
            currSum = max(nums[i], currSum)
            maxSum = max(maxSum, currSum)
            
        
        return maxSum 
        