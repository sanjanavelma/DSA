# Last updated: 19/11/2025, 13:16:05
class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        for i in range(0, len(nums)):
            if original in nums:
                original = original * 2
        return original
        