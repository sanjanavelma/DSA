// Last updated: 17/06/2025, 22:13:28
class Solution {
    public int minBitFlips(int start, int goal) {
        int xor = start ^ goal;
        int count = 0;
        while (xor > 0){
            xor = xor & (xor - 1);
            count++;
        }
        return count;
    }
}