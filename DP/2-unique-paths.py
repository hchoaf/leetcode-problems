# link: https://leetcode.com/problems/unique-paths/
# There is a m X n grid. A robot moves from top-left corner to bottom-right corner.
# The robot can move either right or down. Find the number of unique paths. 


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        # Combination: (m+n-2) C (n-1)
        
        i = m+n-2
        j = n-1
        
        mult = 1
        for _ in range(j):
            mult  = mult * i
            i -= 1
        div = 1
        for _ in range(j):
            div = div * j
            j -= 1
            
        return int(mult/div)
        
        