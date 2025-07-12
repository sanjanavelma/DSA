# Last updated: 12/07/2025, 22:26:02
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        maxi = 0
        for i in range(0, len(nums)):
            if nums[i] == 1:
                count += 1
                maxi = max(maxi, count)
            else:
                count = 0
        return maxi
        