class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        premap = {node: [] for node in range(numCourses)}
        for course, pre in prerequisites:
            premap[course].append(pre)
        
        visiting = set()
        def dfs(course) -> bool:
            if course in visiting:
                return False

            if premap[course] == []:
                return True # possible to complete as there are no prerequisites

            # Add current course
            visiting.add(course)
            
            for pre in premap[course]:
                if not dfs(pre):
                    return False

            visiting.remove(course)
            premap[course] = []
            return True
            

        for c in range(numCourses):
            if not dfs(c):
                return False
        
        return True
