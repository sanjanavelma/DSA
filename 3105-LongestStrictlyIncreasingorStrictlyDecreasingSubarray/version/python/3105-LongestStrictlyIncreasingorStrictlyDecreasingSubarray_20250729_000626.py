# Last updated: 29/07/2025, 00:06:26
class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        stri_inc = 1
        stri_dec = 1
        maxi = 1
        if not nums:
            return 0
        for i in range(0, len(nums) - 1):
            if nums[i] > nums[i + 1]:
                stri_dec += 1
                stri_inc = 1
            elif nums[i] < nums[i + 1]:
                stri_inc += 1
                stri_dec = 1
            else:
                stri_inc = stri_dec = 1
            maxi = max(stri_inc, stri_dec, maxi)
        return maxi
        