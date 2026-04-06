class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        res = []
        subset = []

        def findSubset(index):
            if index >= len(nums):
                res.append(subset.copy())
                return
            
            #pick
            subset.append(nums[index])
            findSubset(index+1)

            #dont pick
            subset.pop()
            findSubset(index+1)

        findSubset(0)
        return res
        