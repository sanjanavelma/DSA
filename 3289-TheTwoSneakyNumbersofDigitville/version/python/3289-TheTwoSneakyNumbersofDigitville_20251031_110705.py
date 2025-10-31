# Last updated: 31/10/2025, 11:07:05
class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        seen = []
        dup = []
        for i in nums:
            if i in seen:
                dup.append(i)
            else:
                seen.append(i)
        return list(set(dup))
