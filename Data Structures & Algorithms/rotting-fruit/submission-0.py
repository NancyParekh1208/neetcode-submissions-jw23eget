class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        # 0 represents empty
        # 1 represents fresh fruit
        # 2 represents rotten fruit
        rotten_queue = collections.deque()
        fresh = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    rotten_queue.append((i,j))
                elif grid[i][j] == 1:
                    fresh += 1 # count number of fresh fruits
        
        dirs = [[-1,0],[0,-1],[1,0],[0,1]] # up, left, down, right

        time = 0

        while fresh > 0 and rotten_queue:
            length  = len(rotten_queue)
            for i in range(length):

                index_row, index_col = rotten_queue.popleft() 

                for direction in dirs:
                    new_row = index_row + direction[0]
                    new_col = index_col + direction[1]
                    
                    if (new_row in range(m) and new_col in range(n) and grid[new_row][new_col] == 1): # this is a fresh fruit
                        grid[new_row][new_col] = 2 # make it rotten
                        rotten_queue.append((new_row,new_col))
                        fresh -= 1
            
            time += 1

        # check if any fresh fruits remain
        return time if fresh == 0 else -1





        