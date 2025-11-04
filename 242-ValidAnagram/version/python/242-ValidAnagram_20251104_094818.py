# Last updated: 04/11/2025, 09:48:18
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            if Counter(s) == Counter(t):
                return True
            else:
                return False

        

        