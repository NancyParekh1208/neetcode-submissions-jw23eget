class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        if not nums:
            return 0

        res = nums[0]
        curr_max = 1
        curr_min = 1

        for num in nums:
            if num == 0:
                curr_max, curr_min = 1,1
                res = max(res, 0)
                continue
            
            temp = curr_max * num
            curr_max = max(curr_min * num, curr_max * num, num)
            curr_min = min(curr_min * num, temp, num)
            
            res = max(curr_max, res)
        
        return res
            