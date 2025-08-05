# Last updated: 05/08/2025, 18:37:49
class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        count = len(fruits)
        for i in range(0, len(fruits)):
            for j in range(0, len(baskets)):
                if fruits[i] <= baskets[j]:
                    count -= 1
                    baskets[j] = 0
                    break
        return count
        