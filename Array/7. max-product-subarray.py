# Link:  https://leetcode.com/problems/maximum-product-subarray/
# Given an array of integers, find a contiguous non-empty subarray with maximum product



# Used Divide and Conquer (O(n logn))
# maximum product of array is either
#    max in left subarray / max in right subarray / max in subarray which lies in both left and right subarray

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        mid = (len(nums)) // 2 
        
        
        left = self.maxProduct(nums[:mid])
        right = self.maxProduct(nums[mid:])
        
        i = mid-1
        j = mid
        temp_left_max, temp_right_max, temp_left_min, temp_right_min = nums[i], nums[j], nums[i], nums[j]
        
        temp = nums[i]
        while i > 0:
            i -= 1
            temp = temp * nums[i]
            temp_left_max = max(temp_left_max, temp)
            temp_left_min = min(temp_left_min, temp)
            
        temp = nums[j]
        while j < len(nums) - 1:
            j += 1
            temp = temp * nums[j]
            temp_right_max = max(temp_right_max, temp)
            temp_right_min = min(temp_right_min, temp)
            
        mix = max(temp_left_max * temp_right_max , temp_left_min * temp_right_min)
        
        
        return max(left, right, mix)
            
        