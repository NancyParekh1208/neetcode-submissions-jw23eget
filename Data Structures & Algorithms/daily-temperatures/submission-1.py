class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        res = [0]*len(temperatures)
        n = len(temperatures)

        for i in range(n-2,-1,-1):
            j = i+1
            while j<n and temperatures[j] <= temperatures[i]:
                if res[j] == 0: # no remaining warmer days so go to end of the array
                    j = n
                    break

                j += res[j] # skip until next warmer day 

            if j<n:
                res[i] = j-i # number of days
        
        return res