# Last updated: 30/06/2025, 12:22:45
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        count = Counter(nums)
        max_len = 0
        for i in count:
            if i + 1 in count:
                max_len = max(max_len, count[i] + count[i + 1])
        return max_len

        