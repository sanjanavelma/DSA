# Last updated: 21/06/2025, 01:51:40
class Solution:
    def isPalindrome(self, s: str) -> bool:
        cs = ''.join(char.lower() for char in s if char.isalnum())
        a = cs[::-1]
        if cs == a:
            return True
        else:
            return False