# Last updated: 03/09/2025, 13:51:16
class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        if len(nums) % 2 != 0:
            return False
        count = Counter(nums)
        for key in count:
            if count[key] % 2 != 0:
                return False
        return True
        