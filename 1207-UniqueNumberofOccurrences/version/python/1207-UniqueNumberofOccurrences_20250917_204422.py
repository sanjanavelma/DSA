# Last updated: 17/09/2025, 20:44:22
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = Counter(arr)
        freq = list(count.values())
        return len(freq) == len(set(freq))
        