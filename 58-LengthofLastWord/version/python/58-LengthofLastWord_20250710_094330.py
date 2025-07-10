# Last updated: 10/07/2025, 09:43:30
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split()
        return len(words[-1])
        