# Last updated: 13/09/2025, 22:13:46
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        l, r = 0, 1
        while l <= r and r < len(nums):
            if nums[l] == 0 and nums[r] != 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r += 1
            elif nums[l] == 0 and nums[r] == 0:
                r += 1
            else:
                l += 1
                r += 1
        