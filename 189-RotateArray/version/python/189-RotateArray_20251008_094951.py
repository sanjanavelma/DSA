# Last updated: 08/10/2025, 09:49:51
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        temp = [0] * n
        for i in range(k):
            temp[i] = nums[n - k + i]
        for i in range(n - k):
            temp[k + i] = nums[i]
        for i in range(n):
            nums[i] = temp[i]