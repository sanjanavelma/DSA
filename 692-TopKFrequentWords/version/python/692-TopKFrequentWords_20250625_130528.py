# Last updated: 25/06/2025, 13:05:28
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = {}
        freq = [[] for i in range(len(words) + 1)]
        for i in words:
            count[i] = 1 + count.get(i, 0)
        for i, cun in count.items():
            freq[cun].append(i)
        res = []
        for i in range(len(freq) -1, 0, -1):
            if freq[i]:
                for s in sorted(freq[i]):
                    res.append(s)
                    if len(res) == k:
                        return res
