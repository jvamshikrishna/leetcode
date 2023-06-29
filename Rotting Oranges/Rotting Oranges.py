from typing import List
from collections import deque

class solution():
    def orangesRotting(self, grid:List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh_oranges = 0
        rotten_count = 0
        minutes =0

        #Find initial rotten oranges and count fresh oranges
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    queue.append((i,j))
                    rotten_count +=1
                elif grid[i][j] == 1:
                    fresh_oranges +=1
        
        # BFS algorithm
        while queue:
            size = len(queue)

            # process all oranges at current time
            for i in range(size):
                x, y = queue.popleft()

                #now explore all 4 directions of the cell (up, down, left, right)
                for dx, dy in [(0,1),(0,-1),(-1,0),(1,0)]:
                    new_x, new_y = x +dx, y +dy

                    # check if adjacent cell is a fresh orange
                    if 0 <= new_x < rows and 0 <= new_y < cols and grid[new_x, new_y]==1:
                        #if above condition satisfies its a fresh fruit make it as rotten
                        grid[new_x, new_y]=2
                        rotten_count += 1
                        fresh_oranges -= 1
                        queue.append((new_x, new_y))
            
            if rotten_count > 0:
                minutes +=1
        # Step 5: Check if there are any fresh oranges remaining        
        if fresh_oranges>0:
            return -1
        
        return minutes-1



