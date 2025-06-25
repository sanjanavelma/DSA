# Last updated: 25/06/2025, 13:15:40
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = Counter(words)

        h = [(-f, w) for w, f in count.items()]
        h.sort()

        ans = [w for f, w in h[:k]]
        return ans
