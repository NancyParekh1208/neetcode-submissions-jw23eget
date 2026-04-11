class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)

        adj = [[] for i in range(n+1)]

        def dfs(node, parentnode):
            if visit[node]:
                return True

            visit[node] = True
            for nei in adj[node]:
                if nei == parentnode:
                    continue
                if dfs(nei, node):
                    return True
            return False
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
            visit = [False] * (n+1) # total 1 - n nodes in the graph

            if dfs(u,-1):
                return [u,v]
        
        return []
        

