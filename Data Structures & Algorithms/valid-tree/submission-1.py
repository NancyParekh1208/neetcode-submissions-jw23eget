class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        adj = [[] for i in range(n)]
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
        
        visit = set()

        def dfs(node, parentnode) -> bool:
            
            if node in visit:
                return False

            visit.add(node) # mark visited
            for nei in adj[node]:
                if nei ==  parentnode:
                    continue
                if not dfs(nei, node):
                    return False

            return True
        
        return dfs(0,-1) and len(visit) == n # since tree has only one component 
