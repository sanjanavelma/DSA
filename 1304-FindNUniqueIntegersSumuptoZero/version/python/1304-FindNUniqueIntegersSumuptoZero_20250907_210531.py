# Last updated: 07/09/2025, 21:05:31
class Solution:
    def sumZero(self, n: int) -> List[int]:
        return [ n * (1 - n) // 2] + list(range(1, n))
        