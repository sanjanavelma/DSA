# Last updated: 30/07/2025, 13:31:11
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        count = Counter(arr)
        uni = [i for i in arr if count[i] == 1]
        if len(uni) < k:
            return ""
        else:
            return uni[k-1]
        