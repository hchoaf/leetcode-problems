# link: https://leetcode.com/problems/palindromic-substrings/
# Given a string, count the number of palindrome substrings inside it.

class Solution:
    def countSubstrings(self, s: str) -> int:
        
        # 2D DP solution:
        #   2D array DP: DP[i][j] is True if s[i:j+1] is a palindrome
        #   count number of cells where DP[i][j] is True
        
        n = len(s)
        
        dp = [[0]*n for _ in range(n)]
        
        
        
        count = 0
        
        palindrome = s[n-1]
        
        
        for i in range(n):
            dp[i][i] = True
            count += 1
        
        
        
        
        
        for l in range(1, n):
            
            for i in range(n-l):
                j = i+l
                if j >= n:
                    continue
                else:
                    if s[i] == s[j]:
                        if l == 1:
                            dp[i][j] = True
                            count += 1
                        else:
                            if dp[i+1][j-1] == True:
                                dp[i][j] = True
                                count += 1
                            
                            
        return count