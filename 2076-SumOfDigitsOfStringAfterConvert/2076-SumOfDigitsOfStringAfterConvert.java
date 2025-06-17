// Last updated: 17/06/2025, 22:13:40
class Solution {
    public int getLucky(String s, int k) {
        // Step 1: Convert the string to its corresponding integer representation
        StringBuilder numStr = new StringBuilder();
        
        for (char c : s.toCharArray()) {
            int value = c - 'a' + 1;
            numStr.append(value);
        }
        
        // Step 2: Perform the sum of digits transformation k times
        for (int i = 0; i < k; i++) {
            int sum = 0;
            for (char digit : numStr.toString().toCharArray()) {
                sum += digit - '0';  // Convert char digit to its numeric value
            }
            numStr = new StringBuilder(String.valueOf(sum));  // Update numStr with the new sum
        }
        
        // Step 3: Return the resulting integer after k transformations
        return Integer.parseInt(numStr.toString());
    }
}
