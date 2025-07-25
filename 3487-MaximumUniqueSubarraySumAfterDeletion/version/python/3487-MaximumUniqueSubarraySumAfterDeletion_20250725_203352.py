# Last updated: 25/07/2025, 20:33:52
class Solution:
    def maxSum(self, nums: List[int]) -> int:
        unique = set(nums)
        res = sum(x for x in unique if x > 0)
        if res == 0:
            return max(unique)
        return res