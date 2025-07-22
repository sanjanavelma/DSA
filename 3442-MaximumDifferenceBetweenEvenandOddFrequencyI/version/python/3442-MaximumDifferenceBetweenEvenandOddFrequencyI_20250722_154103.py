# Last updated: 22/07/2025, 15:41:03
class Solution:
    def maxDifference(self, s: str) -> int:
        even_list = []
        odd_list = []
        count = Counter(s)
        for key, val in count.items():
            if val % 2 == 0:
                even_list.append(val)
            else:
                odd_list.append(val)
        even_max = min(even_list)
        odd_max = max(odd_list)
        return odd_max - even_max