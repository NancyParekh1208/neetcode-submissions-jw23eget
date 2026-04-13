class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = set()
        n = len(candidates)
        candidates.sort()

        def dfs(curr, index, total):
            if total == target:
                res.add(tuple(curr))
                return
            if index >= n or total > target:
                return
            
            curr.append(candidates[index])
            dfs(curr, index+1, total + candidates[index])
            curr.pop()
            while index + 1 < n and candidates[index] == candidates[index+1]:
                index+=1
            dfs(curr, index+1, total)

        dfs([], 0,0)

        return [list(combination) for combination in res]
        