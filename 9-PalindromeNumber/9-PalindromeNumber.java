// Last updated: 17/06/2025, 22:14:51
class Solution {
    public boolean isPalindrome(int x) {
        if(x<0){
            return false;
        }
        int orginal = x;
        int reverse = 0;

        while(x != 0){
            int digit = x % 10;
            reverse = reverse * 10 + digit;
            x /= 10;
        }
        return orginal == reverse;
    }
}