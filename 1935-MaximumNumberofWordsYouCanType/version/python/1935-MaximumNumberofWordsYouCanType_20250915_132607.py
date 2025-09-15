# Last updated: 15/09/2025, 13:26:07
class Solution:
    def canBeTypedWords(self, text: str, b: str) -> int:
        return sum(1 for w in text.split() if not any(c in b for c in w))


        