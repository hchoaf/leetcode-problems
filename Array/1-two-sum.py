# Link: https://leetcode.com/problems/two-sum/
# Given an array and target integer, return indices of the two numbers in the array that add up to target.



class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # Solution using hashmap.
        # For each element in the array, put (List[index], index) as key,value pair in hashmap dictioanry. O(n)
        # Iterate through each element in the array. Check if complement is in hashmap, and if index != value, return. O(n) * O(1)
        
        hashmap = {}
        
        for i in range(len(nums)):
            hashmap[nums[i]] = i
            
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap and i != hashmap[complement]:
                return [i, hashmap[complement]]