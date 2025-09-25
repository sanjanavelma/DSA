# Last updated: 25/09/2025, 23:36:32
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        count1 = Counter(word1)
        count2 = Counter(word2)
        if set(count1.keys()) != set(count2.keys()):
            return False
        if sorted(count1.values()) != sorted(count2.values()):
            return False
        return True