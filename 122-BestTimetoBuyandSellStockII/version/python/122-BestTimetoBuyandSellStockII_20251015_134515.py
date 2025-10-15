# Last updated: 15/10/2025, 13:45:15
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        summ = 0
        for i in range(0, len(prices) - 1):
            if prices[i] < prices[i + 1]:
                summ += prices[i + 1] - prices[i]
        return summ

        