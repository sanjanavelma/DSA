# Last updated: 30/09/2025, 13:47:49
class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        while len(nums) > 1:
            newNums = []
            for i in range(0, len(nums)-1):
                if len(nums) == 1:
                    return nums[0]
                else:
                    newNums.append((nums[i] + nums[i + 1]) % 10)
            nums = newNums
        return nums[0]

        