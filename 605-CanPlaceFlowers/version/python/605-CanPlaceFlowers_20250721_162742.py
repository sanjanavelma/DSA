# Last updated: 21/07/2025, 16:27:42
class Solution:
    def canPlaceFlowers(self, fl: List[int], n: int) -> bool:
        count = 0
        for i in range(0, len(fl)):
            if fl[i] == 0:
                left = ((i == 0) or fl[i - 1] == 0)
                right = ((i == len(fl) - 1) or fl[i + 1] == 0)
                if left and right:
                    fl[i] = 1
                    count += 1
                    if count >= n:
                        return True
        return count >= n
