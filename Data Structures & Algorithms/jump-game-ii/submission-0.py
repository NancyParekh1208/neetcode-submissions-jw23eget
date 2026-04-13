class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        l,r = 0,0 # Tell us the window

        while r < n-1:
            farthest = 0
            for i in range(l,r+1):
                farthest = max(farthest, i + nums[i]) # how far we can actually jump
            l = r+1
            r = farthest
            res += 1
        
        return res



