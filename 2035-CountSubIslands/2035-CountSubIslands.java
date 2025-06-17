// Last updated: 17/06/2025, 22:13:42
class Solution {
    public int countSubIslands(int[][] grid1, int[][] grid2) {
        int m = grid1.length;
        int n = grid1[0].length;
        int count = 0;

        // First, remove any part of grid2 that cannot be a sub-island
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid2[i][j] == 1 && grid1[i][j] == 0) {
                    // Sink the island in grid2 that cannot be a sub-island
                    sink(grid2, i, j, m, n);
                }
            }
        }

        // Count remaining sub-islands
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid2[i][j] == 1) {
                    count++;
                    sink(grid2, i, j, m, n);
                }
            }
        }

        return count;
    }

    // Helper function to sink the island in grid2
    private void sink(int[][] grid, int i, int j, int m, int n) {
        if (i < 0 || i >= m || j < 0 || j >= n || grid[i][j] == 0) {
            return;
        }

        // Mark this cell as visited by sinking it
        grid[i][j] = 0;

        sink(grid, i - 1, j, m, n);
        sink(grid, i + 1, j, m, n);
        sink(grid, i, j - 1, m, n);
        sink(grid, i, j + 1, m, n);
    }
}
