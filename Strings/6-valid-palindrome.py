# Link: https://leetcode.com/problems/valid-palindrome/
# Check if the given string is a valid palindrome, considering only alphanumeric characters case insenstiive


class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        i = 0
        j = len(s)-1
        
        
        while (i < j):
            while(i<j and not s[i].isalnum()):
                i += 1
            while(i<j and not s[j].isalnum()):
                j -= 1
            
            
            if s[i].lower() != s[j].lower():
                
                return False
            
            
            i += 1
            j -= 1
        
        return True
            
                