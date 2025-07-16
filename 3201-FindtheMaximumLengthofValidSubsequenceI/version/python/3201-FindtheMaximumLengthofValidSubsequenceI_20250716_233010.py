# Last updated: 16/07/2025, 23:30:10
class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        even = 0
        odd = 0
        for i in nums:
            if i % 2 == 0:
                even += 1
            else:
                odd += 1
        even_me = 0
        odd_me = 0
        for i in nums:
            if i % 2 == 0:
                even_me = max(even_me, odd_me + 1)
            else:
                odd_me = max(even_me + 1, odd_me)
        return max(even, odd, even_me, odd_me)

                
        