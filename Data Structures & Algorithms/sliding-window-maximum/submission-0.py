class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        for i in range(len(nums)-k+1):
            maxInWindow = max(nums[i:i+k])
            res.append(maxInWindow)
        return res

        