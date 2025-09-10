# Last updated: 10/09/2025, 14:53:44
class Solution:
    def canPlaceFlowers(self, fl: List[int], n: int) -> bool:
        f = [0] +fl+ [0]
        for i in range(1, len(f) - 1):
            if f[i - 1] == 0 and f[i] == 0 and f[i + 1]== 0:
                f[i] = 1
                n -= 1
        return n <= 0
