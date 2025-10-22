# Last updated: 23/10/2025, 01:04:07
class Solution:
    def isPalindrome(self, s: str) -> bool:
        cs = ''.join([char for char in s if char.isalnum()]).lower()
        if cs == cs[::-1]:
            return True
        else:
            return False