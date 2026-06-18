class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:

        n = len(nums)
        ans = []
        ans.extend(nums)
        ans.extend(nums)
        return ans