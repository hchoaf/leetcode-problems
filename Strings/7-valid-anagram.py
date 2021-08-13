# Link: https://leetcode.com/problems/valid-anagram/
# Return true if s is an anagram of t, else false


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            if sorted(s) == sorted(t):
                return True
            
        return False
        