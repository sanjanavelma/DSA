# Last updated: 13/10/2025, 13:36:46
class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        for i in range(len(words)-1, 0, -1):
            if sorted(words[i]) == sorted(words[i - 1]):
                del words[i]
        return words
