# Link: https://leetcode.com/problems/coin-change/submissions/
# Given target amount and a list of coins, return the fewest number of coins 
#  that is needed to make up that amount

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        coin_dict = {}
        for coin in coins:
            coin_dict[coin] = 1
        
        
        
        dp = [-1 for i in range(amount+1)]
        
        dp[0] = 0
        
        for i in range(1, amount+1):
            if i in coin_dict:
                dp[i] = 1
            else:
                val = -1
                for coin in coin_dict:
                    if i-coin > 0 and dp[i-coin] != -1 and (val == -1 or val > (1+dp[i-coin])):
                        val = 1 + dp[i-coin]
                        if val == 2:
                            break
                dp[i] = val
        
        
        return dp[amount]
        
        