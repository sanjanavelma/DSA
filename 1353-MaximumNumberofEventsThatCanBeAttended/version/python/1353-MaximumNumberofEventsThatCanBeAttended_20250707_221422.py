# Last updated: 07/07/2025, 22:14:22
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        count = Counter(arr)
        cand = [num for num, freq in count.items() if num == freq]
        return max(cand) if cand else -1

        