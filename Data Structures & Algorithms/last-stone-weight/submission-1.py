class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        # First make min heap
        stones = [-stone for stone in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            # take two largest stones
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)
            
            if abs(x-y) > 0:
                heapq.heappush(stones, -abs(x-y))
        
        if len(stones) == 1:
            return -stones[0]
        
        return 0


        