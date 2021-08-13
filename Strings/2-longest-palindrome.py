# Link: https://leetcode.com/problems/longest-palindromic-substring/submissions/
# Given a string, return the longest palindrome substring

class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        # 2D DP solution:
        #   2D array DP: DP[i][j] is True if s[i:j+1] is a palindrome
        
        n = len(s)
        
        dp = [[0]*n for _ in range(n)]
        
        
        
        longest = 1
        palindrome = s[n-1]
        
        
        for i in range(n):
            dp[i][i] = True
        
        
        
        
        
        for l in range(1, n):
            
            for i in range(n-l):
                j = i+l
                if j >= n:
                    continue
                else:
                    if s[i] == s[j]:
                        if l == 1:
                            dp[i][j] = True
                            palindrome = s[i:j+1]
                        else:
                            if dp[i+1][j-1] == True:
                                dp[i][j] = True
                                palindrome = s[i:j+1]
                            
                            
        return palindrome