class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {node: [] for node in range(numCourses)}
        for course, pre in prerequisites:
            preMap[course].append(pre)

        # store all the courses along the current DFS path
        visiting = set()

        def dfs(course) -> bool:
            if course in visiting:
                return False # cycle detected
            
            if preMap[course] == []:
                return True
            
            visiting.add(course)
            for pre in preMap[course]:
                if not dfs(pre):
                    return False
            
            visiting.remove(course)
            preMap[course] = [] # mark as done
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        
        return True