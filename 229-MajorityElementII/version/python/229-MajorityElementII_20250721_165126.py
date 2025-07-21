# Last updated: 21/07/2025, 16:51:26
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = []
        count = Counter(nums)
        n = len(nums) / 3
        for key, val in count.items():
            if val > n:
                res.append(key)
        return res