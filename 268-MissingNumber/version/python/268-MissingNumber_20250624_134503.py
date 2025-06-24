# Last updated: 24/06/2025, 13:45:03
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        nums = sorted(nums)
        for i in range(0, len(nums)):
            if nums[i] != i:
                return i
        return n