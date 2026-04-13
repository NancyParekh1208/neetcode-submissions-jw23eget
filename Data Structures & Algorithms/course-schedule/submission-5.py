class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adj = {node:[] for node in range(numCourses)}
        for course, requiredCourse in prerequisites:
            adj[course].append(requiredCourse)

        visiting  = set() # to check for cycles

        def dfs(course):
            if course in visiting:
                return False
            
            if adj[course] == []: # this means there is not required numCourses
                return True
            
            visiting.add(course)

            for pre in adj[course]:
                if not dfs(pre):
                    return False

            visiting.remove(course)
            adj[course] = [] # because it was not having cycle it's possible to complete the prereq
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        
        return True