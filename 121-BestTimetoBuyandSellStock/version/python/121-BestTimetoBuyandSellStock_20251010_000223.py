# Last updated: 10/10/2025, 00:02:23
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        pmax = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                pmax = max(pmax, profit)
            else:
                l = r
            r += 1
        return pmax
        