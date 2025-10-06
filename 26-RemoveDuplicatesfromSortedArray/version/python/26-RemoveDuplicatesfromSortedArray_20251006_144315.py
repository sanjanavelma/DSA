# Last updated: 06/10/2025, 14:43:15
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        expectedNums = []
        if not nums:
            return 0
        write_index = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[write_index] = nums[i]
                write_index += 1
        return write_index