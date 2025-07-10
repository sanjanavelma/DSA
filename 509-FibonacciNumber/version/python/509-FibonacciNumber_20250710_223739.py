# Last updated: 10/07/2025, 22:37:39
from functools import lru_cache

@lru_cache(maxsize=None)
class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        return self.fib(n-1) + self.fib(n-2)
