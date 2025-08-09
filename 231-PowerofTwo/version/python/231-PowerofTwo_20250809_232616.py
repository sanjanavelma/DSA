# Last updated: 09/08/2025, 23:26:16
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and not (n & (n - 1))