class Solution(object):
    def orangesRotting(self,grid):
        # Define the directions for adjacent cells (up, down, left, right)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        rotten = set()
        fresh_count = 0
        minutes = 0

        # Step 1: Initialize the set and count the fresh oranges
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:  # Rotten orange
                    rotten.add((i, j))
                elif grid[i][j] == 1:  # Fresh orange
                    fresh_count += 1

        # Step 3: Perform BFS
        while fresh_count > 0 and rotten:
            new_rotten = set()
            for row, col in rotten:
                for dx, dy in directions:
                    new_row, new_col = row + dx, col + dy
                    if (
                        0 <= new_row < len(grid) and
                        0 <= new_col < len(grid[0]) and
                        grid[new_row][new_col] == 1  # Fresh orange
                    ):
                        grid[new_row][new_col] = 2  # Mark as rotten
                        new_rotten.add((new_row, new_col))
                        fresh_count -= 1

            rotten = new_rotten
            minutes += 1

        # Step 4: Check for remaining fresh oranges
        if fresh_count > 0:
            return -1

        # Step 5: Return the minimum number of minutes
        return minutes