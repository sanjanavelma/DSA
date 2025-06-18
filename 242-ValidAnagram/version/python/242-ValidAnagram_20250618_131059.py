# Last updated: 18/06/2025, 13:10:59
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            if Counter(s) == Counter(t):
                return True
            else:
                return False

        

        