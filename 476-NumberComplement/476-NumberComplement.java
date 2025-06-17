// Last updated: 17/06/2025, 22:14:18
class Solution {
    public int findComplement(int num) {
        // Step 1: Create a mask with all bits set to 1 that is the same length as the binary representation of num
        int mask = 1;
        while (mask < num) {
            mask = (mask << 1) | 1;
        }
        
        // Step 2: XOR num with the mask to get the complement
        return num ^ mask;
    }
}
