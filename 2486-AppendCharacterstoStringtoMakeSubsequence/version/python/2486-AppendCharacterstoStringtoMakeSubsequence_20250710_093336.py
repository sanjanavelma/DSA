# Last updated: 10/07/2025, 09:33:36
class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i = 0
        for char in s:
            if i < len(t) and t[i] == char:
                i += 1
        if i == len(t):
            return 0
        else:
            return len(t) - i