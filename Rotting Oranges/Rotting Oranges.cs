public class Solution {
    public int OrangesRotting(int[][] grid) {
        // Define the directions for adjacent cells (up, down, left, right)
        int[][] directions = new int[][] {
            new int[] {-1, 0},
            new int[] {1, 0},
            new int[] {0, -1},
            new int[] {0, 1}
        };

        int rows = grid.Length;
        int cols = grid[0].Length;
        int freshCount = 0;
        int minutes = 0;

        // Step 1: Initialize the queue and count the fresh oranges
        Queue<int[]> queue = new Queue<int[]>();
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (grid[i][j] == 2) {  // Rotten orange
                    queue.Enqueue(new int[] {i, j});
                } else if (grid[i][j] == 1) {  // Fresh orange
                    freshCount++;
                }
            }
        }

        // Step 3: Perform BFS
        while (freshCount > 0 && queue.Count > 0) {
            int size = queue.Count;
            for (int i = 0; i < size; i++) {
                int[] orange = queue.Dequeue();
                int row = orange[0];
                int col = orange[1];
                foreach (int[] direction in directions) {
                    int newRow = row + direction[0];
                    int newCol = col + direction[1];
                    if (newRow >= 0 && newRow < rows && newCol >= 0 && newCol < cols &&
                        grid[newRow][newCol] == 1) {  // Fresh orange
                        grid[newRow][newCol] = 2;  // Mark as rotten
                        queue.Enqueue(new int[] {newRow, newCol});
                        freshCount--;
                    }
                }
            }
            if (queue.Count > 0) {
                minutes++;
            }
        }

        // Step 4: Check for remaining fresh oranges
        if (freshCount > 0) {
            return -1;
        }

        // Step 5: Return the minimum number of minutes
        return minutes;
    }
}
