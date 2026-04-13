class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        tickets.sort()
        n = len(tickets)
        res = ['JFK'] # starting point intialized
        adj = {src : [] for src,dst in tickets}
        for src, dst in tickets:
            adj[src].append(dst)

        def dfs(node):
            if len(res) == n + 1:
                return True
            if node not in adj:
                return False

            temp = list(adj[node])
            for i, v in enumerate(temp):
                adj[node].pop(i)
                res.append(v)
                if dfs(v):
                    return True
                adj[node].insert(i,v)
                res.pop()
            
            return False

        dfs('JFK')
        return res