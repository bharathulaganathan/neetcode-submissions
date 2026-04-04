class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = [prices[0]]
        sell = [prices[-1]]
        profit = 0
        for i in range(1, len(prices)):
            buy.append(min(prices[i], buy[-1]))
            sell.append(max(prices[-(i+1)], sell[-1]))
        for j in range(len(prices)-1):
            profit = max(profit, sell[-(j+2)] - buy[j])
        return profit
        