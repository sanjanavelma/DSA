# Last updated: 21/06/2025, 23:12:54
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
        