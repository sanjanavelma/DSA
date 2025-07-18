# Last updated: 18/07/2025, 09:25:02
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res = []
        for i in words:
            for j in range(0, len(words)):
                if words[j] in i and len(words[j]) != len(i):
                    res.append(words[j])
        result = list(set(res))
        return result