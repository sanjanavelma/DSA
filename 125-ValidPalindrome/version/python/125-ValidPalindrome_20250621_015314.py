# Last updated: 21/06/2025, 01:53:14
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join([char for char in s if char.isalnum()]).lower()
        if s == s[::-1]:
            return True 
        else:
            return False
