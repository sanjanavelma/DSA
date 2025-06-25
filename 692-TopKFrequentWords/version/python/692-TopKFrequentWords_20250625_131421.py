# Last updated: 25/06/2025, 13:14:21
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = Counter(words)
        res = sorted(count.keys(), key = lambda word: (-count[word], word))
        return res[:k]