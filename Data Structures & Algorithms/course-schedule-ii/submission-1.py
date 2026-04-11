class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        adj = [[] for i in range(numCourses)]
        for src, dst in prerequisites:
            adj[dst].append(src)
            indegree[src] += 1 # increase indegree
        
        q = collections.deque()
        for n in range(numCourses):
            if indegree[n] == 0: # Add only courses with no remaining prerequisites
                q.append(n)

        res = []
        while q:
            node = q.popleft()
            res.append(node)

            for neighbor in adj[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)

        return res if len(res) == numCourses else []