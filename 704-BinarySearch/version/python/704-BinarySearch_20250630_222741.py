# Last updated: 30/06/2025, 22:27:41
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)
        while l < r:
            mid = l + ((r - l) // 2)
            if nums[mid] >= target:
                r = mid
            elif nums[mid] < target:
                l = mid + 1
        return l if (l < len(nums)and nums[l] == target) else -1