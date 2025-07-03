# Last updated: 04/07/2025, 01:23:57
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = Counter(nums)
        return max(count, key=count.get)
        