# link: https://leetcode.com/problems/contains-duplicate/submissions/

# return true if array contains any duplicates else false

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        return False if len(set(nums)) == len(nums) else True
        