class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(curr, total, index):

            if index >= len(nums) or total > target:
                # invalid sequence
                return
            
            if total == target:
                res.append(curr.copy())
                return

            curr.append(nums[index])
            dfs(curr, total + nums[index], index) # same number

            curr.pop()
            dfs(curr, total, index+1)


        dfs([], 0, 0)
        return res
        