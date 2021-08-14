# Link: https://leetcode.com/problems/climbing-stairs/
# It takes 'n' steps to reach the top of a staircase. You can either climb 1 or 2 steps. How many distinct ways can you climb to the top?

class Solution:
    def climbStairs(self, n: int) -> int:
        ans = [0, 1, 2]
        
        if n == 1:
            return ans[1]
        if n == 2:
            return ans[2]
        
        for i in range(3, n+1):
            ans.append(ans[i-1] + ans[i-2])
        
        return ans[n]