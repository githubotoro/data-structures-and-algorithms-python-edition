class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = prices[0]

        for idx in range(1, len(prices)):
            sell = prices[idx] - buy

            profit = max(profit, sell)

            buy = min(buy, prices[idx])

        return profit
