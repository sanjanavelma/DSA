# Last updated: 23/06/2025, 23:06:56
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        index = 0
        for i in range(0, len(nums)):
            if nums[i] != val:
                nums[index] = nums[i]
                index += 1
        return index


        