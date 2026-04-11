class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        n = len(edges)
        visited = [False]*(n+1)
        cycle = set()
        cycleStart = -1

        adj = [[] for i in range(n+1)]

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def dfs(node, parent):
            nonlocal cycleStart
            if visited[node]:
                cycleStart = node
                return True
            
            visited[node] = True
            for nei in adj[node]:
                if nei == parent:
                    continue
                if dfs(nei, node):
                    if cycleStart != -1:
                        cycle.add(node)
                    if cycleStart == node:
                        cycleStart = -1
                    return True
            
            return False
        
        dfs(1,-1)

        for u,v in reversed(edges):
            if u in cycle and v in cycle:
                return [u,v]
        
        return []