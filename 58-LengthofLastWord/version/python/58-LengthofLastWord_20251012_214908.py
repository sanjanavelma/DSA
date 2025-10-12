# Last updated: 12/10/2025, 21:49:08
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split()
        return len(words[-1])
        