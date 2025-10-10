# Last updated: 10/10/2025, 13:59:19
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ind = 1
        dup = 0
        prev = nums[0]
        for i in range(1, len(nums)):
            if nums[i] != prev:
                dup = 0
            else:
                dup += 1
            if dup <= 1:
                nums[ind] = nums[i]
                ind += 1
                prev = nums[i]
        return ind
        