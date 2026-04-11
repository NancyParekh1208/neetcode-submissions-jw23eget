class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Topological sorting 
        premap = {node: [] for node in range(numCourses)}

        for course, pre in prerequisites:
            premap[course].append(pre)

        cycle, visiting = set(), set()
        processed = []

        def dfs(course):
            if course in cycle:
                return False
            if course in visiting:
                return True
            
            cycle.add(course)
            for pre in premap[course]:
                if dfs(pre) == False:
                    return False

            cycle.remove(course)
            visiting.add(course)
            processed.append(course)
            return True

        for course in range(numCourses):
            if dfs(course) == False:
                return []

        return processed
        