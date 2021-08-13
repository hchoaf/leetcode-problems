#Link: https://leetcode.com/problems/group-anagrams/
# Given an array of strings, group the anagrams together. e.g) bat, atb, tab

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        
        # Created a dictionary where key = sorted(strings) and values are strings
        
        
        d = {}
       
        for strings in strs:
            sorted_string = str(sorted(strings))
            if sorted_string not in d:
                d[sorted_string] = [strings]
            else:
                d[sorted_string].append(strings)
                
        return list(d.values())
        
        
        