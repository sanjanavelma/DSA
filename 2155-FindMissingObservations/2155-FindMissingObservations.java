// Last updated: 17/06/2025, 22:13:35
class Solution {
    public int[] missingRolls(int[] rolls, int mean, int n) {
        // Calculate the sum of the given rolls
        int sum_m = 0;
        for (int roll : rolls) {
            sum_m += roll;
        }
        
        // Total sum we need for n + m rolls
        int total_sum = mean * (n + rolls.length);
        
        // Calculate the sum of the missing rolls
        int sum_n = total_sum - sum_m;
        
        // Check if the sum_n can be distributed among n rolls
        if (sum_n < n || sum_n > 6 * n) {
            // It's impossible to distribute the sum_n
            return new int[0];
        }
        
        // Create an array to hold the missing rolls
        int[] missing = new int[n];
        
        // Start by assigning 1 to each missing roll (the minimum value)
        int quotient = sum_n / n;
        int remainder = sum_n % n;
        
        // Fill the missing array
        for (int i = 0; i < n; i++) {
            missing[i] = quotient;
            if (remainder > 0) {
                missing[i]++;
                remainder--;
            }
        }
        
        return missing;
    }
}
