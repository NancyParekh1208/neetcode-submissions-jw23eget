class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        count  = 0

        adj = [[] for node in range(n)]

        # create adjacentancy list for mthe undirected graph
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])

        visited = [0] * n

        def dfs(node):

            if visited[node] == 1:
                return

            # mark as visited
            visited[node] = 1

            for nei in adj[node]:
                dfs(nei)
            

        for i in range(n):
            if visited[i] == 0:
                dfs(i)
                count += 1

        return count       

        