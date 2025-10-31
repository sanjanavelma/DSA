# Last updated: 31/10/2025, 11:55:55
class Solution:
    def smallestNumber(self, n: int) -> int:
        r = 0
        while n > 0:
            r = r * 2 + 1
            n //= 2
        return r
        