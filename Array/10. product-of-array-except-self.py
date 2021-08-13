# Link: https://leetcode.com/problems/product-of-array-except-self/submissions/

# For a given array of integers, return an array such that ans[i] is equal to the product of all elements except ans[i]
# DO NOT use division operator.


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # first find products left to each element
        
        left_product = [1]
        temp = 1
        for i in range(len(nums)-1):
            temp *= nums[i]
            left_product.append(temp)
        
        
        # now we multiply products right to each element on left_product
        
        right_product = 1
        for i in range(len(left_product)-1, -1, -1):
            left_product[i] *= right_product
            right_product *= nums[i]
            
        return left_product
    