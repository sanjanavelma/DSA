# Last updated: 03/09/2025, 14:06:34
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        a = {}
        count = 0
        for i in nums:
            if i in a:
                count += a[i]
                a[i] += 1
            else:
                a[i] = 1
        return count


        