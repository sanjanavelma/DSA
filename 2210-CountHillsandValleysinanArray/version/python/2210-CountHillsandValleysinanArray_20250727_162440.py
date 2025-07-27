# Last updated: 27/07/2025, 16:24:40
class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        count = 0
        uni = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                uni.append(nums[i])
        for i in range(1, len(uni) - 1):
            if uni[i - 1] < uni[i] > uni[i +1] or uni[i - 1] > uni[i] < uni[i + 1]:
                count += 1
        return count



        