class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        index = -1
        for i in range(len(gas)):
            
            tank = gas[i] - cost[i]
            if tank < 0:
                continue
            
            j = (i+1) % len(gas) # if i = n-1 then j will be 0
            while j!=i:
                tank += gas[j]
                tank -= cost[j]
                if tank < 0:
                    break # circuit will not be completed

                j+=1
                j%=len(gas)
            
            if j == i:
                return i
            
        return -1