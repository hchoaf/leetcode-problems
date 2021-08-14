# link: https://leetcode.com/problems/house-robber/
# Given an array of integers, nums[i] refer to amount of money we can rob in i'th house.
# If we rob 2 consecutive houses, police comes.
# Find max amount of money we can rob.


class Solution:
    def rob(self, nums: List[int]) -> int:
        
        
        # dp[i] = max amount of money that we can rob, given that we have a list of houses houses[:i+1]
        
        n = len(nums)
        dp = [0 for _ in range(n)]
        for i in range(n):
            if i == 0:
                dp[i] = nums[i]
            elif i == 1:
                dp[i] = max(nums[i], nums[i-1])
            else:
                dp[i] = max(dp[i-1], nums[i] + dp[i-2])
                
        return dp[n-1]
        