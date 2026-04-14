class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        freq = {}
        for i in range(len(nums)):
            key = nums[i]
            freq[key] = freq.get(key, 0) + 1
            if freq[key] > 1:
                return True
        
        return False