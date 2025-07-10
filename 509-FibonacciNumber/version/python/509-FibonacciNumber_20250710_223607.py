# Last updated: 10/07/2025, 22:36:07
class Solution:
    def fib(self, n: int) -> int:
        a, b = 0, 1
        for i in range(n):
           a, b = b, a + b
        return a

        