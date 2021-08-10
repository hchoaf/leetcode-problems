# Link: https://leetcode.com/problems/3sum/submissions/

# Given an array of numbers, return all triplets num[i], num[j], num[k] such that i != j != k and adds up to 0.
# Solution must not contain duplicate triplets

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        ans = []
        nums.sort()
        
        for i in range(len(nums) - 2):
            if i>0 and nums[i] == nums[i-1]:
                continue
            else:
                j = i+1
                k = len(nums) - 1
                
                while(j < k):
                    s = nums[i] + nums[j] + nums[k]
                    
                    if s > 0: # we need to add smaller element
                        k -= 1
                    elif s < 0: # we need to add larger element
                        j += 1
                    else:
                        ans.append([nums[i], nums[j], nums[k]])
                        
                        # we must skip if same j or same k
                        
                        while j < k and nums[j] == nums[j+1]:
                            j += 1
                        while j < k and nums[k] == nums[k-1]:
                            k -= 1
                        
                        # after skipping, check next elements
                        j += 1
                        k -= 1
        
        
        return ans
                        
                
        
        