# Link:https://leetcode.com/problems/decode-ways/
# Alphabets are given codes (A = 1, B = 2, .. Z = 26)
# Given an integer, determine the number of alphabets that can be decoded from the integer code


class Solution:
    def numDecodings(self, s: str) -> int:
        
        
        
        # Suppose we have code 2 2 0 1 X X X X ......
        # We iterate from back and fill in the DP table from the back
        # Now let's say we've reached the first '2'.
        # If the first character is '0', then dp is 0.
        # If not, we first copy the previous dp value (because we can always use the first character as a single codeword)
        # If the first two codes '2 2' this case, fit into the condition (10 ~ 26), we add the previous previous dp value.
        # For instance, dp for 2 2 0 1 X X X X is, dp (for 2, 2 0 1 X X X X) plus dp (for 2 2, 0 1 X X X X)
        
        
        
        n = len(s)
        dp = [0 for _ in range(n+1)]
        
        
        
        
        
        dp[n-1] = 1 if s[n-1] != '0' else 0
        dp[n] = 1    
            
        for i in range(n-2, -1, -1):
            if s[i] == '0':
                dp[i] = 0
                
            else:
                dp[i] = dp[i+1]
                if i < n-1 and (s[i] == '1' or s[i] == '2' and s[i+1] < '7'):
                    dp[i] += dp[i+2]
        print(dp)
        return dp[0]