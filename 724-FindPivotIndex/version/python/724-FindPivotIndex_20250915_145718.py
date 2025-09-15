# Last updated: 15/09/2025, 14:57:18
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

        