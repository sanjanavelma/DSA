# Last updated: 10/07/2025, 22:17:20
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        org = x
        rev = 0
        while x > 0:
            rev = rev * 10 + x % 10
            x //= 10
        return org == rev

        