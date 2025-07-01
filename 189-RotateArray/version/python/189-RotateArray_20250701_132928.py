# Last updated: 01/07/2025, 13:29:28
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        for i in range(k):
            nums.insert(0,nums[-1])
            nums.pop()
