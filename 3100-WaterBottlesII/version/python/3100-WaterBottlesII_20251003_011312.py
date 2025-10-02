# Last updated: 03/10/2025, 01:13:12
class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        ans = numBottles
        while numBottles >= numExchange:
            numBottles -= numExchange - 1
            numExchange += 1
            ans += 1
        return ans
        