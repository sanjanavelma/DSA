# Last updated: 10/09/2025, 14:49:46
class Solution:
    def kidsWithCandies(self, candies: List[int], ex: int) -> List[bool]:
        fin = [True] * len(candies)
        for i in range(0, len(candies)):
            if candies[i] + ex < max(candies):        
                fin[i] = False
        return fin