class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        adj =[[] for i in range(len(points))]
        n = len(points)
        minHeap = [(0,0)]
        for i in range(len(points)):
            for j in range(i+1, len(points)):
              
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                adj[i].append([j, dist]) # create weighted graph
                adj[j].append([i, dist])

        total = 0
        visited = set()

        while len(visited) < n:
            cost, node = heapq.heappop(minHeap)
            if node in visited:
                continue
            if node not in visited:
                visited.add(node)
                total += cost
                for nei, neiCost in adj[node]:
                    heapq.heappush(minHeap, (neiCost,nei))

        return total