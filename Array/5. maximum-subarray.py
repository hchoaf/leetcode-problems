
# Link: https://leetcode.com/problems/maximum-subarray/submissions/

# Given an array of numbers, find the maximum value of a subarray

class Solution:
        def maxSubArray(self, nums: List[int]) -> int:
        
                
            # Suppose we know max value for A[1... i-1]
            # Now we have array A[1... i]
            # maximum is either: the previous max in A[1... i-1] OR a max where subarray ends with A[i]
            #    why? there can't be a different max that does not end with A[i], because it would have already been assessed in A[1... i-1]
            # then, max where subarray ends with A[i] is simply max(max that ends with A[i-1] + A[i], A[i])
            
            # so, as we iterate i from 0 to n, we need to keep record of:
            #   Current max AND current max that ends with A[i]
            if len(nums) == 1:
                return nums[0]
            
            curr_max = nums[0]
            max_ends_with = nums[0]
            
            for i in range(1, len(nums)):
                max_ends_with = max(nums[i], max_ends_with + nums[i])
                curr_max = max(curr_max, max_ends_with)
            
            return curr_max