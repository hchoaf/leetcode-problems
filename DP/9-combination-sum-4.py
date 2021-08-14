# Link: https://leetcode.com/problems/combination-sum-iv/
# Given a list of nums and target integer, return the number of possible 'permutations' that add up to the target int.

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        num_dict = {}
        
        for num in nums:
            num_dict[num] = 1
        
        
        dp = [0 for i in range(target + 1)]
        
        for i in range(1, target + 1):
            if i in num_dict:
                dp[i] += 1
            for num in num_dict:
                if i-num > 0:
                    dp[i] += dp[i-num]
                    
                    
        return(dp[target])
            
        