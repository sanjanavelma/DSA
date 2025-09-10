# Last updated: 10/09/2025, 14:51:39
class Solution:
    def kidsWithCandies(self, candies: List[int], extra: int) -> List[bool]:
        currmax = max(candies)
        ans = []
        for i in candies:
            if currmax <= i+extra:
                ans.append(True)
            else:
                ans.append(False)
        
        return ans