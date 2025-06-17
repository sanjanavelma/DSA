// Last updated: 17/06/2025, 22:13:43
class Solution {
    public int chalkReplacer(int[] chalk, int k) {
        // Step 1: Calculate the total chalk consumption
        long totalChalk = 0;
        for (int c : chalk) {
            totalChalk += c;
        }
        
        // Step 2: Reduce k modulo the total chalk consumption
        k %= totalChalk;
        
        // Step 3: Find the student who will replace the chalk
        for (int i = 0; i < chalk.length; i++) {
            if (k < chalk[i]) {
                return i;
            }
            k -= chalk[i];
        }
        
        return -1; // This line should never be reached
    }
}
