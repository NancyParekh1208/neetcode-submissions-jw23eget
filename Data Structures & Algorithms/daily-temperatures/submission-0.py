class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        N = len(temperatures)
        stack = []
        res = [0]*N
        for i, temp in enumerate(temperatures):
            
            while stack and stack[-1][0] < temp:
                t, index = stack.pop()
                res[index] = i-index
            
            stack.append((temp,i))
        
        return res

        