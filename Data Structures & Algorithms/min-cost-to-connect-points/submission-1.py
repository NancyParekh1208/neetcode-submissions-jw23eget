class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        dist = [10000000] * n
        visit = [False] * n
        edges, res = 0, 0
        node = 0 # start from random node
        while edges < n-1:
            visit[node] = True
            nextNode = -1
            for i in range(n):
                if visit[i]:
                    continue
                
                curDist = (abs(points[node][0]- points[i][0]) + abs(points[node][1]- points[i][1]))
                dist[i] = min(dist[i], curDist)

                if nextNode == -1 or dist[i] < dist[nextNode]:
                    nextNode = i

            res += dist[nextNode]
            node = nextNode
            edges+=1
        return res