# Link: https://leetcode.com/problems/word-break/
# Given a string and a dictionary of words, return true if the string can be segmented int oa space-separated sequence of one or more dict words

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        
        
        # iterate string from s[0] to s[0:i] to s[0:len(s)]
        # For a given string, check if it is in the wordDict
        #   IF not, for words in wordDict, check if dp[0:i-len(w)] is true (can be made of words in wordDict), and the remaining string is in wordDict
        
        
        
        
        d = {}
        n = len(s)
        for words in wordDict:
            d[words] = 1
        
        dp = [False for i in range(n)]
        
        
        for i in range(n):
            if s[:i+1] in d:
                dp[i] = True
            else:
                for words in d:
                    w = len(words)
                    if dp[i-w] and s[i-w+1:i+1] == words:
                        dp[i] = True
                        break
                
        return dp[n-1]