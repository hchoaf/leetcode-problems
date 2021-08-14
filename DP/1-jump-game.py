# Link: https://leetcode.com/problems/jump-game/
# Jump game. Given an array of integers, array[index] indicates how much steps you can jump at that position (if 3, than can jump 1,2,3 steps)
# Determine whether you can reach the end of the array


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        
        # Start from the last position
        # Check previous step. If we can reach current position from previous step, move current to previous and previous to previous -1
        #                      If not, move previous to -1 and leave current unchanged
     
        
        
        last = len(nums) - 1
        current = last - 1
        
        
        while current >= 0:
            if current + nums[current] >= last:
                last = current
                current -= 1
            else:
                current -= 1
                
        return True if last == 0 else False
                    
        