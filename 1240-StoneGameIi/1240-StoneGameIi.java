// Last updated: 17/06/2025, 22:13:56
class Solution {

    public int stoneGameII(int[] piles) {
        int n = piles.length;
        int[] suffixSum = new int[n + 1];
        int[][] dp = new int[n][n + 1];
        
        // Calculate the suffix sums
        for (int i = n - 1; i >= 0; i--) {
            suffixSum[i] = suffixSum[i + 1] + piles[i];
        }
        
        // Start the recursive DFS from the first pile with M = 1
        return dfs(0, 1, piles, suffixSum, dp);
    }
    
    private int dfs(int i, int M, int[] piles, int[] suffixSum, int[][] dp) {
        if (i >= piles.length) {
            return 0; // No more piles left
        }
        if (dp[i][M] != 0) {
            return dp[i][M]; // Return the already computed result
        }
        
        int maxStones = 0;
        // Try taking X piles where 1 <= X <= 2 * M
        for (int X = 1; X <= 2 * M; X++) {
            if (i + X <= piles.length) {
                // Calculate the maximum stones Alice can get
                maxStones = Math.max(maxStones, suffixSum[i] - dfs(i + X, Math.max(M, X), piles, suffixSum, dp));
            }
        }
        
        dp[i][M] = maxStones;
        return maxStones;
    }
    
    public static void main(String[] args) {
        Solution solution = new Solution();
        
        int[] piles1 = {2, 7, 9, 4, 4};
        System.out.println(solution.stoneGameII(piles1)); // Output: 10
        
        int[] piles2 = {1, 2, 3, 4, 5, 100};
        System.out.println(solution.stoneGameII(piles2)); // Output: 104
    }
}
