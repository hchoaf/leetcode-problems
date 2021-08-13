# Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/submissions/

# Given a list of stock prices, find the best profit you can make by buying once and selling once.




class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        profit = 0
        local_min = prices[0]
        for i in range(1, len(prices)):
            profit = max(profit, prices[i] - local_min)
            local_min = min(local_min, prices[i])
            
        return profit
            
        