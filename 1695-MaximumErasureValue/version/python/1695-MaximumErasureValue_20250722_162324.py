# Last updated: 22/07/2025, 16:23:24
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        unique = set()
        sums = 0
        res = 0
        start = 0
        for i in range(0, len(nums)):
            while nums[i] in unique:
                unique.remove(nums[start])
                sums -= nums[start]
                start += 1
            sums += nums[i]
            unique.add(nums[i])
            res = max(res, sums)
        return res

        