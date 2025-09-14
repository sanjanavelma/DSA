# Last updated: 14/09/2025, 11:11:09
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        c = 0
        a, b = 0, len(nums) - 1
        while a < b:
            if (nums[a] + nums[b]) == k:
                c += 1
                a += 1
                b -= 1
            elif(nums[a] + nums[b]) < k:
                a += 1
            else: b -= 1
        return c
