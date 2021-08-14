# Link: https://leetcode.com/problems/house-robber-ii/
# Same as house robbing question, but now houses are circular (last and first house are considered adjacent)


class Solution:
    def rob(self, nums: List[int]) -> int:
        
        
        # 2 DP: One for houses[:n], another for houses[1:n+1]
        # and find max(ans1, ans2)
        
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return nums[0] if nums[0] > nums[1] else nums[1]
        dp = [0 for _ in range(n-1)]
        dp2 = [0 for _ in range(n-1)]
        for i in range(n-1):
            if i == 0:
                dp[i] = nums[i]
                dp2[i] = nums[i+1]
            elif i == 1:
                dp[i] = max(nums[i], nums[i-1])
                dp2[i] = max(nums[i+1], nums[i])
            else:
                dp[i] = max(dp[i-1], nums[i] + dp[i-2])
                dp2[i] = max(dp2[i-1], nums[i+1] + dp2[i-2])
                
        return max(dp[n-2], dp2[n-2])
        
        
        
        