class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Topological sorting (Kahn's algorithm)

        indegree = [0] * numCourses
        adj = [[] for i in range(numCourses)]
        for src, dst in prerequisites:
            
            indegree[dst]+=1
            adj[src].append(dst)

        q = deque()
        for node in range(numCourses):
            if indegree[node] == 0: # This course is not a prerequisite for other courses 
                q.append(node)
        finish = 0
        while q:
            node = q.popleft()
            finish += 1
            for nei in adj[node]:
                indegree[nei]-=1
                if indegree[nei] == 0:
                    q.append(nei)
        
        return finish == numCourses
