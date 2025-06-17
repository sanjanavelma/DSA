// Last updated: 17/06/2025, 22:13:37
class Solution {
    public int[][] construct2DArray(int[] original, int m, int n) {
        // Check if the total number of elements matches m * n
        if (original.length != m * n) {
            return new int[0][0]; // Return an empty 2D array
        }
        
        // Create the 2D array
        int[][] result = new int[m][n];
        
        // Fill the 2D array with elements from the original array
        for (int i = 0; i < original.length; i++) {
            result[i / n][i % n] = original[i];
        }
        
        return result;
    }
}
