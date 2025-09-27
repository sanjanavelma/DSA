# Last updated: 27/09/2025, 14:01:53
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        c = 0
        for k in range(n - 1, 1, -1):
            i, j = 0, k - 1
            while i < j:
                if nums[i] + nums[j] > nums[k]:
                    c += (j - i)
                    j -= 1
                else:
                    i += 1
        return c
        