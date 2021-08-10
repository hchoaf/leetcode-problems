# Link: https://leetcode.com/problems/container-with-most-water/

# Array's elements' index-value pair (index, value) represents the location and height of a wall.
# Select 2 walls so that it can store the most amount of water.


class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left = 0
        right = len(height) - 1
        
        
        # start with the widest container, and iterate down.
        # suppose we have height such that (0,1), (1,2), (2,3), (3,4), (5,6) where (location, height)
        # Then, if we start from container (0,1)-(5,6), we don't need to check contaniners (0,1)-(1,2) ~ (0,1)-(3,4)
        
        for width in range(len(height)-1, 0, -1):
            if height[left] < height[right]:
                max_area = max(height[left] * width, max_area)
                left += 1
            else:
                max_area = max(height[right] * width, max_area)
                right -= 1
        
        return max_area