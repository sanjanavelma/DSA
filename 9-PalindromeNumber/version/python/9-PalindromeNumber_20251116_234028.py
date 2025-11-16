# Last updated: 16/11/2025, 23:40:28
class Solution:
    def isPalindrome(self, x: int) -> bool:
        #s = str(x)
        #return s == s[::-1]
        if x < 0:
            return False
        org = x
        rev = 0
        while x > 0:
            rev = rev * 10 + x % 10
            x //= 10
        return org == rev

        