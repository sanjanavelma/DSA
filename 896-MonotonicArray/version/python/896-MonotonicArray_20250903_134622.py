# Last updated: 03/09/2025, 13:46:22
class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        inc = True
        dec = True
        for i in range(0, len(nums) - 1):
            if nums[i] > nums[i + 1]:
                inc = False
            if nums[i] < nums[i + 1]:
                dec = False
        return inc or dec


        