# Last updated: 29/07/2025, 09:18:20
class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        summ = nums[0]
        maxi = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                summ += nums[i]
            else:
                summ = nums[i]
            maxi = max(summ, maxi)
        return maxi
        