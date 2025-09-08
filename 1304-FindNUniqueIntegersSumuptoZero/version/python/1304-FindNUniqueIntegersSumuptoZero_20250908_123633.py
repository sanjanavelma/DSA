# Last updated: 08/09/2025, 12:36:33
class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        def c(x):
            return '0' not in str(x)
        for i in range(1, n):
            a = n - i
            if c(i) and c(a):
                return [i, a]
        