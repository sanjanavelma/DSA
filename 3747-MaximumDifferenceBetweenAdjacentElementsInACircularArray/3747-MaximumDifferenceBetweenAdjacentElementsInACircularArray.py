# Last updated: 17/06/2025, 22:13:11
class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        max_diff = 0
        for i in range(len(nums)):
            diff = abs(nums[i] - nums[(i + 1) % len(nums)])
            if max_diff < diff:
                max_diff = diff
        return max_diff
