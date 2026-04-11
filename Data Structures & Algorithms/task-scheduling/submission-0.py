class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # first find the frequency of each task
        count = [0] * 26
        for task in tasks:
            count[ord(task) - ord('A')] += 1
        
        count.sort()
        maxf = count[25] # largest freq
        idle = (maxf-1)*n
        for i in range(24, -1, -1):
            idle -= min(maxf - 1, count[i])
        
        return max(0, idle) + len(tasks)