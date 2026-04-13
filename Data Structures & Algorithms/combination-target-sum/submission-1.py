class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        n = len(nums)
        res = []

        def dfs(curr, index, total):
            nonlocal res
            if total == target:
                res.append(curr.copy())
                return
            if index >= n or total > target:
                return
            # pick current value
            curr.append(nums[index])
            dfs(curr, index, total + nums[index])
            # not pick
            curr.pop()
            dfs(curr, index+1, total)


        dfs([],0,0)

        return res