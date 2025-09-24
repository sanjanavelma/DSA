# Last updated: 24/09/2025, 22:34:25
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n, l, z, a = len(nums), 0, 0, 0
        for r, x in enumerate(nums):
            z += (x==0)
            if z > 1:
                z -= (nums[l]==0)
                l += 1
            a = max(a, r - l)
        return a