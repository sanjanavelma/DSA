# Last updated: 29/07/2025, 09:55:53
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        l = 0
        r = sum(nums) 
        for i, v in enumerate(nums):
            r -= v
            if l == r:
                return i
            l += v
        return -1

        